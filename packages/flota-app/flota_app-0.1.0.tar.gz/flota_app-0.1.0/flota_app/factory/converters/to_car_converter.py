from typing import Self

from flota_app.factory.converters.converter import Converter
from flota_app.models.car import Car


class ToCarsConverter(Converter):
    def convert(self, data: list[dict[str, Car]]) -> list[Car]:
        """
        :param data: list of dict representations of car
        :return: list of Cars
        """
        return [Car.from_dict(element) for element in data]

    def __eq__(self, other: Self) -> bool:
        return type(self) == type(other)
