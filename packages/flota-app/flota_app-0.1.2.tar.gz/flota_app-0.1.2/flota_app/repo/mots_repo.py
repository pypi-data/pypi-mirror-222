from typing import Any

from easy_crud_repo_service.repo.crud_repo import CrudRepo
from easy_crud_repo_service.repo.connections.builders import MySQLConnectionPoolBuilder


import logging

from flota_app.models.mots.basic_mot import BasicMot
from flota_app.models.mots.mot import Mot

logging.basicConfig(level=logging.INFO)


class BasicMotsRepo(CrudRepo):
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
        super().__init__(MySQLConnectionPoolBuilder(env_path).build(), BasicMot)

    def update_many(self, items: list[Mot]) -> list[Any]:

        resuts = []
        for item in items:
            resuts.append(self.update(item.id, item))
        return resuts
