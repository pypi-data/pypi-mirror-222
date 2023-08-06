from dataclasses import dataclass
from datetime import date
from typing import Any, Self


@dataclass
class Car:
    """
    id, registration_number, first_registration_date, vin, brand, model
    Default values are set to None because of design pattern 'Builder'
    """
    id: int = None
    registration_number: str = None
    first_registration_date: date = None
    vin: str = None
    brand: str = None
    model: str = None

    def __post_init__(self) -> None:
        """
        Checks if first_registration_date is date or iso representation of it,
        and if it happens to be true then parse it to date object
        """
        if self.first_registration_date and type(self.first_registration_date) == str:
            self.first_registration_date = date.fromisoformat(self.first_registration_date)

    def update_id(self, id_: int) -> None:
        """ Updates id using new one """
        self.id = id_

    def update_registration_number(self, new_registration_number: str) -> None:
        """ Updates registration numer using new one """
        self.registration_number = new_registration_number

    def update_first_registration_date(self, new_first_registration_date: str) -> None:
        """ Updates first_registration_date using new one """
        self.first_registration_date = new_first_registration_date

    def update_vin(self, new_vin: str) -> None:
        """ Updates vin using new one """
        self.vin = new_vin

    def update_brand(self, new_brand: str) -> None:
        """ Updates brand using new one """
        self.brand = new_brand

    def update_model(self, new_model: str) -> None:
        """ Updates model using new one """
        self.model = new_model


    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        """ Creates new Car object using provided dict. Awaits json dict, so any data type used has to parseable """
        return cls(
            int(data["id"]),
            data["registration_number"],
            date.fromisoformat(data["first_registration_date"]),
            data["vin"],
            data["brand"],
            data["model"]
        )

    @classmethod
    def attr_names(cls) -> list[str]:
        """ Returns attribute names as list. Used in CrudRepo """
        return ['id', 'registration_number', 'first_registration_date', 'vin', 'brand', 'model']
