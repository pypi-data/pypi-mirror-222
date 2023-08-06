from dataclasses import dataclass
from datetime import date
from typing import Self

from flota_app.models.mots.basic_mot import BasicMot


@dataclass
class BasicMotBuilder:
    def __init__(self) -> None:
        self._mot = BasicMot()

    def set_id(self, new_id: int) -> Self:
        self._mot.id = new_id
        return self

    def set_mot_code(self, new_mot_code: str) -> Self:
        self._mot.mot_code = new_mot_code
        return self

    def set_start_date(self, new_start_date: date) -> Self:
        self._mot.start_date = new_start_date
        return self

    def set_car_id(self, new_car_id: int) -> Self:
        self._mot.car_id = new_car_id
        return self

    def set_type(self, new_type: str) -> Self:
        self._mot.type = new_type
        return self

    def build(self) -> BasicMot:
        return self._mot
