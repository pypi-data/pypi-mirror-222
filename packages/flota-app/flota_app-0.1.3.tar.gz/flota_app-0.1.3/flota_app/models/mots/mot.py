import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Self

@dataclass
class Mot(ABC):
    """
    id: int | None - primary key of insurance
    mot_code: str | None - unique identifier of mot, created by mot station
    start_date: datetime.date | None - date that mot starts to be vaild
    car_id: int | None - id of mot'ed Car object
    type: str | None - type of mot

    All values have default value of None because of Builder project pattern accept type - this attribute is set to
    "Dealership"
    """

    id: int | None = None
    mot_code: str = None
    start_date: datetime.date | None = None
    car_id: int | None = None
    type: str | None = None

    def __post_init__(self) -> None:
        """ Makes sure that when date is stored as iso date str, it will be parsed to date object"""
        if self.start_date and type(self.start_date) == str:
            self.start_date = datetime.date.fromisoformat(self.start_date)

    def deadline(self) -> datetime.date:
        """ Template method that implements solution for calculation of duration of mot"""
        return self.mot_start() + self.duration()

    @abstractmethod
    def mot_start(self) -> datetime.date:
        """ How mot start date will be obtained? """
        pass

    @abstractmethod
    def duration(self) -> datetime.timedelta:
        """ How duration will be calculated?"""
        pass

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        """
        :param data: dict with attr name as key, and attr value as value
        :return: Mot
        """
        return cls(
            int(data["id"]),
            data['mot_code'],
            datetime.date.fromisoformat(data["start_date"]),
            int(data['car_id'])
        )

    @classmethod
    def attr_names(cls) -> list[str]:

        return ['id', 'mot_code', 'start_id', 'car_id', 'type']

