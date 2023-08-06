from typing import Any, Dict, Iterator, Mapping, Optional, Tuple

from ._table_key import DataKey
from ._table_row import DataRow


class TableKeyError(Exception):
    """
    Raised when inconsistent keys are inserted into a table.
    """

    pass


class DataTable(Mapping[DataKey, DataRow]):
    def __init__(self, record_id: str):
        super().__init__()
        self._record_id = record_id
        self._rows: Dict[DataKey, DataRow] = {}
        self._key_fields: Optional[Tuple[str, ...]] = None

    @property
    def record_id(self) -> str:
        return self._record_id

    def get(self, pk: DataKey, create=False) -> Optional[DataRow]:
        row = self._rows.get(pk)
        if row is None and create:
            row = self._rows[pk] = DataRow(pk)
        return row

    def put_value(self, pk: DataKey, field_id: str, value: Any) -> None:
        self.__check_key(pk)
        row = self.get(pk, create=True)
        row[field_id] = value

    def put_values(self, pk: DataKey, **kwargs) -> None:
        self.__check_key(pk)
        row = self.get(pk, create=bool(kwargs))
        for k, v in kwargs.items():
            row[k] = v

    def get_value(self, pk: DataKey, field_id: str) -> Any:
        row = self.get(pk)
        if row is None:
            return None
        return row.get(field_id)

    def __check_key(self, pk: DataKey) -> None:
        if self._key_fields is None:
            self._key_fields = pk.keys()
        elif self._key_fields != pk.keys():
            raise TableKeyError("Inconsistent key fields")

    def __getitem__(self, pk: DataKey) -> DataRow:
        return self._rows[pk]

    def __len__(self) -> int:
        return len(self._rows)

    def __iter__(self) -> Iterator[DataKey]:
        return iter(self._rows)
