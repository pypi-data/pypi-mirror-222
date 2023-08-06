import datetime
from dataclasses import dataclass

from flota_app.models.mots.mot import Mot

@dataclass
class BasicMot(Mot):
    type: str | None = 'Basic'

    def mot_start(self) -> datetime.date:
        """ Uses BasicMot.start_date"""
        return self.start_date

    def duration(self) -> datetime.timedelta:
        """ For basic mot duration is 365 days"""
        return datetime.timedelta(365)


