import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Self


@dataclass
class Insurance(ABC):
    """
    id: int | None - primary key of insurance
    insurance_code: str | None - unique identifier of insurance, created by insurance company
    start_date: datetime.date | None - date that insurance starts to be vaild
    car_id: int | None - id of insured Car object
    type: str | None - type of insurance

    All values have default value of None because of Builder project pattern
    """
    id: int | None = None
    insurance_code: str | None = None
    start_date: datetime.date | str | None = None
    car_id: int | None = None
    type: str | None = None

    def __post_init__(self) -> None:
        """ Makes sure that when date is stored as iso date str, it will be parsed to date object"""
        if self.start_date and type(self.start_date) == str:
            self.start_date = datetime.date.fromisoformat(self.start_date)

    def deadline(self) -> datetime.date:
        """ Template method that implements solution for calculation of duration of insurance"""
        return self.insurance_start() + self.duration()

    @abstractmethod
    def insurance_start(self) -> datetime.date:
        """ How insurance start date will be obtained? """
        pass

    @abstractmethod
    def duration(self) -> datetime.timedelta:
        """ How duration will be calculated?"""
        pass

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        """

        :param data: dict with attr name as key, and attr value as value
        :return: Instance of insurance
        """
        return cls(
            int(data["id"]),
            data["insurance_code"],
            datetime.date.fromisoformat(data["start_date"]),
            int(data['car_id'])
        )

    @classmethod
    def attr_names(cls) -> list[str]:
        return ['id', 'insurance_code', 'start_id', 'car_id', 'type']