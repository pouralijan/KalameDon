#!/usr/bin/env python3

from enum import Enum

class Level(Enum):
    A1: int = 1 
    A2: int = 2 
    B1: int = 3 
    B2: int = 4 
    C1: int = 5 
    C2: int = 6 

class Vocabulary:
    def __init__(self, vocabulary: str) -> None:
        self.__vocabulary: str = vocabulary
        self.__i_know: bool = False
        self.__definition: str = ''
        self.__level: Level = None
        self.__examples: list = []

    def __str__(self) -> str:
        return self._Vocabulary__vocabulary

    def set_i_know(self) -> None:
        self._Vocabulary__i_know = True

    def is_i_know(self) -> bool:
        return self._Vocabulary__i_know

    def set_definition(self, definition: str) -> None:
        self._Vocabulary__definition = definition

    def get_definition(self) -> str:
        return self._Vocabulary__definition

    def set_level(self, level: Level) -> None:
        if isinstance(level, Level):
            self._Vocabulary__level = level
        elif isinstance(level, int):
            self._Vocabulary__level = Level(level)
        else:
            message = f'Can\'t convert \'{type(level)}\' to Level implicitly'
            raise TypeError(message)

    def get_level(self) -> Level:
        return self._Vocabulary__level

    def add_example(self, example: str or list) -> None:
        if isinstance(example, list):
            self._Vocabulary__examples.extend(example)
        else:
            self._Vocabulary__example.append(example)

    def get_examples(self) -> list:
        return self._Vocabulary__examples
