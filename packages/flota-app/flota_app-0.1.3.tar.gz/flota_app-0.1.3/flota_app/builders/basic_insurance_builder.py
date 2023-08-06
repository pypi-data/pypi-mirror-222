from dataclasses import dataclass
from datetime import date
from typing import Self

from flota_app.models.insurances.basic_insurance import BasicInsurance


@dataclass
class BasicInsuranceBuilder:
    def __init__(self) -> None:
        self._insurance = BasicInsurance()

    def set_id(self, new_id: int) -> Self:
        self._insurance.id = new_id
        return self

    def set_insurance_code(self, new_insurance_code: str) -> Self:
        self._insurance.mot_code = new_insurance_code
        return self

    def set_start_date(self, new_start_date: date) -> Self:
        self._insurance.start_date = new_start_date
        return self

    def set_car_id(self, new_car_id: int) -> Self:
        self._insurance.car_id = new_car_id
        return self

    def set_type(self, new_type: str) -> Self:
        self._insurance.type = new_type
        return self

    def build(self) -> BasicInsurance:
        return self._insurance
