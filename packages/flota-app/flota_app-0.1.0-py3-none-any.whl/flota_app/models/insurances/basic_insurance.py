import datetime
from dataclasses import dataclass

from flota_app.models.insurances.insurance import Insurance

@dataclass
class BasicInsurance(Insurance):
    """
    id: int | None - primary key of insurance
    insurance_code: str | None - unique identifier of insurance, created by insurance company
    start_date: datetime.date | None - date that insurance starts to be vaild
    car_id: int | None - id of insured Car object
    type: str | None - type of insurance

    All values have default value of None because of Builder project pattern accept type - this attribute is set to
    "Basic"
    """
    type: str = 'Basic'

    def insurance_start(self) -> datetime.date:
        """ Uses BasicInsurance.start_date"""
        return self.start_date

    def duration(self) -> datetime.timedelta:
        """ For basic insurance duration is 365 days"""
        return datetime.timedelta(365)

