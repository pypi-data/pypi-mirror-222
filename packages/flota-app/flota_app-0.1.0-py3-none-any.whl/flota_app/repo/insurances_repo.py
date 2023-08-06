from typing import Any

from easy_crud_repo_service.repo.crud_repo import CrudRepo
from easy_crud_repo_service.repo.connections.builders import MySQLConnectionPoolBuilder

import logging

from flota_app.models.insurances.basic_insurance import BasicInsurance
from flota_app.models.insurances.insurance import Insurance

logging.basicConfig(level=logging.INFO)


class BasicInsurancesRepo(CrudRepo):
    """
    Extends CrudRepo. Used to provide user with CRUD sql transactions
    env_path - path to .env file that contains connections parameters. Example:
        POOL_NAME=MYSQL_POOL
        POOL_SIZE=5
        POOL_RESET_SESSION=True
        HOST=localhost
        DATABASE=database
        USER=your_user
        PASSWORD=your_password
        PORT=3306
    """
    def __init__(self, env_path: str):
        super().__init__(MySQLConnectionPoolBuilder(env_path).build(), BasicInsurance)

    def update_many(self, items: list[Insurance]) -> list[Any]:
        """
        Updates multiple entities
        :param items: list of Insurances
        :return: list of Insurances ids that were obtained
        """
        resuts = []
        for item in items:
            resuts.append(self.update(item.id, item))
        return resuts
