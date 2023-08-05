import math
from typing import List

import numpy as np
from tqdm import tqdm

from ..data_managers.semantic_header import RecordConstructor
from ..database_managers.db_connection import DatabaseConnection
from ..data_managers.datastructures import ImportedDataStructures
from ..utilities.performance_handling import Performance
from ..cypher_queries.data_importer_ql import DataImporterQueryLibrary as di_ql
import pandas as pd


class Importer:
    def __init__(self, db_connection: DatabaseConnection, data_structures: ImportedDataStructures,
                 records: List["RecordConstructor"], batch_size: int,
                 use_sample: bool = False, use_preprocessed_files: bool = False,
                 perf: Performance = None):
        self.connection = db_connection
        self.structures = data_structures.structures
        self.records = records

        self.batch_size = batch_size
        self.use_sample = use_sample
        self.use_preprocessed_files = use_preprocessed_files
        self.perf = perf

    def _write_message_to_performance(self, message: str):
        if self.perf is not None:
            self.perf.finished_step(activity=message)

    def import_data(self) -> None:
        for structure in self.structures:
            labels = structure.labels
            file_directory = structure.file_directory
            # read in all file names that match this structure
            for file_name in structure.file_names:
                # read and import the nodes
                df_log = structure.read_data_set(file_directory, file_name, use_sample=self.use_sample,
                                                 use_preprocessed_file=self.use_preprocessed_files)
                df_log["justImported"] = True
                self._import_nodes_from_data(labels, df_log, file_name)

                self._write_message_to_performance(f"Imported data from table {structure.name}: {file_name}")

            if structure.has_datetime_attribute():
                # once all events are imported, we convert the string timestamp to the timestamp as used in Cypher
                self._reformat_timestamps(structure)
                self._write_message_to_performance(
                    f"Reformatted timestamps from events from event table {structure.name}: {file_name}")

            self._filter_nodes(structure=structure)  # filter nodes according to the structure
            self._write_message_to_performance(
                f"Filtered the nodes from table {structure.name}: {file_name}")

            self._finalize_import(labels=labels)  # removes temporary properties

            self._write_message_to_performance(
                f"Finalized the import from table {structure.name}: {file_name}")

    def _reformat_timestamps(self, structure):
        datetime_formats = structure.get_datetime_formats()
        for attribute, datetime_format in datetime_formats.items():
            if datetime_format.is_epoch:
                self.connection.exec_query(di_ql.get_convert_epoch_to_timestamp_query,
                                           **{
                                               "label": structure.get_label_string(),
                                               "attribute": attribute,
                                               "datetime_object": datetime_format,
                                               "batch_size": self.batch_size
                                           })

            self.connection.exec_query(di_ql.get_make_timestamp_date_query,
                                       **{
                                           "label": structure.get_label_string(),
                                           "attribute": attribute, "datetime_object": datetime_format,
                                           "batch_size": self.batch_size
                                       })

    def _filter_nodes(self, structure):
        for boolean in (True, False):
            attribute_values_pairs_filtered = structure.get_attribute_value_pairs_filtered(exclude=boolean)
            for name, values in attribute_values_pairs_filtered.items():
                self.connection.exec_query(di_ql.get_filter_events_by_property_query,
                                           **{"prop": name, "values": values, "exclude": boolean})

    def _finalize_import(self, labels):
        # finalize the import
        self.connection.exec_query(di_ql.get_finalize_import_events_query,
                                   **{
                                       "labels": labels,
                                       "batch_size": self.batch_size
                                   })

    def _import_nodes_from_data(self, labels, df_log, file_name):
        # start with batch 0 and increment until everything is imported
        batch = 0
        print("\n")
        pbar = tqdm(total=math.ceil(len(df_log) / self.batch_size), position=0)
        while batch * self.batch_size < len(df_log):
            pbar.set_description(f"Loading data from {file_name} from batch {batch}")

            # import the events in batches, use the records of the log
            batch_without_nans = [{k: int(v) if isinstance(v, np.integer) else v for k, v in m.items()
                                   if (isinstance(v, list) and len(v) > 0) or (not pd.isna(v) and v is not None)}
                                  for m in
                                  df_log[batch * self.batch_size:(batch + 1) * self.batch_size].to_dict(
                                      orient='records')]
            self.connection.exec_query(di_ql.get_create_nodes_by_importing_batch_query,
                                       **{"batch": batch_without_nans, "labels": labels})
            self._create_records()

            pbar.update(1)
            batch += 1
        pbar.close()

    def _create_records(self) -> None:
        for record_constructor in self.records:
            self.connection.exec_query(di_ql.get_create_record_query,
                                       **{
                                           "record_constructor": record_constructor,
                                           "batch_size": self.batch_size
                                       })
            self.connection.exec_query(di_ql.get_reset_added_label_query,
                                       **{
                                           "record_constructor": record_constructor,
                                           "batch_size": self.batch_size
                                       })
        self.connection.exec_query(di_ql.get_mark_records_as_done_query,
                                   **{
                                       "batch_size": self.batch_size
                                   })
