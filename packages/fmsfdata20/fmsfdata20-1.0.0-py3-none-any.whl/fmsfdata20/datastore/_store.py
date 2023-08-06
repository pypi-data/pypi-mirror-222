from typing import Any, Dict, Optional

from ._table import DataTable
from ._table_key import DataKey
from ._table_row import DataRow


class DataStore:
    def __init__(self):
        self._tables: Dict[str, DataTable] = {}

    def put_value(self, record_id: str, key: DataKey, field_id: str, value: Any):
        """
        Put a value into the datastore
        """
        table = self.get_table(record_id, create=True)
        table.put_value(key, field_id, value)

    def put_values(self, record_id: str, key: DataKey, /, **kwargs):
        """
        Put multiple values into the datastore for the same key
        """
        if not kwargs:
            return
        table = self.get_table(record_id, create=True)
        table.put_values(key, **kwargs)

    def get_value(self, record_id: str, key: DataKey, field_id: str) -> Any:
        """
        Retrieves a specific value from the datastore
        :param record_id:
        :param field_id:
        :param key:
        :return:
        """
        row = self.get_row(record_id, key)
        if not row:
            return None

        return row.get(field_id)

    def get_table(self, record_id: str, create=False) -> DataTable:
        table = self._tables.get(record_id)
        if table is None and create:
            table = self._tables[record_id] = DataTable(record_id=record_id)
        return table

    def get_row(self, record_id: str, key: DataKey) -> Optional[DataRow]:
        table = self.get_table(record_id)
        if not table:
            return None
        return table.get(key)

    def __getitem__(self, record_id: str) -> DataTable:
        return self._tables[record_id]

    def __len__(self):
        return len(self._tables)
