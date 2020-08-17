"""
-*- coding: utf-8 -*-
"""

from enum import Enum


class DataBaseEngines(Enum):
    SQLite = 0
    MYSql = 1
    Redis = 2

class ConnectionHandler:
    pass


class BaseDataBaseEngine:
    def __init__(self):
        raise NotImplementedError

    def __del__(self):
        raise NotImplementedError

    def connect(self):
        raise NotImplementedError

    def insert(self):
        raise NotImplementedError

    def select(self):
        raise NotImplementedError


class SQLiteDataBaseEngine(BaseDataBaseEngine):
    pass


class MariaDBDataBaseEngine(BaseDataBaseEngine):
    pass


class RedisDataBaseEngine(BaseDataBaseEngine):
    pass


class DataBaseManager:
    def __init__(self, databases):
        for database in databases:
            print(database)


class DataBase:
    def __init__(self, databases: dict):
        self.__database_manager = DataBaseManager(databases)








