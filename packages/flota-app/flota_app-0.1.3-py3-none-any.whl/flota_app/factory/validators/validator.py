from abc import ABC, abstractmethod
from typing import Any


class Validator(ABC):
    """ Abstract class of Validator"""
    @abstractmethod
    def validate(self, data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """ How data will be validated """
        pass
