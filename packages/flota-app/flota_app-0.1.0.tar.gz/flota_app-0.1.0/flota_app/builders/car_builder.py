from dataclasses import dataclass
from datetime import date
from typing import Self

from flota_app.models.car import Car


@dataclass
class CarBuilder:
    def __init__(self) -> None:
        self._car = Car()

    def set_id(self, new_id: int) -> Self:
        self._car.id = new_id
        return self

    def set_registration_number(self, new_registration_numer: str) -> Self:
        self._car.registration_number = new_registration_numer
        return self

    def set_first_registration_date(self, new_registration_date: date) -> Self:
        self._car.first_registration_date = new_registration_date
        return self

    def set_vin(self, new_vin: str) -> Self:
        self._car.vin = new_vin
        return self

    def set_brand(self, new_brand: str) -> Self:
        self._car.brand = new_brand
        return self

    def set_model(self, new_model: str) -> Self:
        self._car.model = new_model
        return self

    def build(self) -> Car:
        return self._car
