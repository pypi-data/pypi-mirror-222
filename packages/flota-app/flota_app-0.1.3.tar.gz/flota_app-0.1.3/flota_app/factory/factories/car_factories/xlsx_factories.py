from dataclasses import dataclass
from typing import Any

from easyvalid_data_validator.constraints import Constraint

from flota_app.factory.factories.data_factory import DataFactory
from flota_app.factory.converters.to_car_converter import ToCarsConverter
from flota_app.factory.loaders.xlsx_loader import XlsxDataLoader
from flota_app.factory.validators.json_dict_validator import JsonDictValidator


@dataclass
class FromXlsxToCarsWithExpectedConstraintsDataFactory(DataFactory):
    """
    path: path of xlsx file that has to load cars information

    constraints: dict that keys are names that will be validated and values are dict that has
        easyvalid_data_validator.constraints.Constraint objects as key and constraint (for example regex).
    Example of constraints dict:
    constraints = {
        "id": {Constraint.INT_GRATER: 0},
        "registration_number": {Constraint.STRING_REGEX: r"^[A-Z0-9]{7}$"},
        "first_registration_date": {Constraint.STRING_REGEX: r"^.*$"},
        "brand": {Constraint.STRING_REGEX: r"^.*$"},
        "model": {Constraint.STRING_REGEX: r"^.*$"}

    csv_sep: has default value of ',', defines delimiter used in file
    """
    path: str
    constraints: dict[str, dict[Constraint, Any]]

    def create_data_loader(self):
        """ Creates XlsxDataLoader """
        return XlsxDataLoader(self.path)

    def create_validator(self):
        """ Creates JsonDictValidator using self. constraints """
        return JsonDictValidator(self.constraints)

    def create_converter(self):
        """ Creates ToCarsConverter """
        return ToCarsConverter()
