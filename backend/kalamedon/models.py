from django.db import models
from enum import Enum
from django.contrib.auth.models import User

# Create your models here.


class Level(Enum):
    A1: int = 1
    A2: int = 2
    B1: int = 3
    B2: int = 4
    C1: int = 5
    C2: int = 6


class KalameDon(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.name


class Vocabulary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kalamedon = models.ForeignKey(KalameDon, on_delete=models.CASCADE)

    vocabulary: models.CharField = models.CharField(
        max_length=255, primary_key=True)

    i_know: models.BooleanField = models.BooleanField(default=False)
    definition: models.TextField = models.TextField()
    level: models.IntegerField = models.IntegerField()
    examples: models.TextField = models.TextField()

    def __str__(self) -> models.CharField:
        return self.vocabulary

    def set_i_know(self) -> None:
        self.i_know = True

    def is_i_know(self) -> models.BooleanField:
        return self.i_know

    def set_definition(self, definition: str) -> None:
        self.definition = definition

    def get_definition(self) -> str:
        return self.definition

    def set_level(self, level: Level) -> None:
        if isinstance(level, Level):
            self.level = level
        elif isinstance(level, int):
            self.level = Level(level)
        else:
            message = f"Can't convert '{type(level)}' to Level implicitly"
            raise TypeError(message)

    def get_level(self) -> Level:
        return self.level

    def add_example(self, example: str or list) -> None:
        if isinstance(example, list):
            self.examples.extend(example)
        else:
            self.example.append(example)

    def get_examples(self) -> list:
        return self.examples
