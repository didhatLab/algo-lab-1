from tests.base import BaseAlgoCases
from generator.first_generator import first_matrix_generator
from generator.second_generator import second_generator_matrix


class TestFirstGen(BaseAlgoCases.TestsForAllMatrixGenerators):

    def setUp(self) -> None:
        self.generator = first_matrix_generator


class TestSecondGen(BaseAlgoCases.TestsForAllMatrixGenerators):

    def setUp(self) -> None:
        self.generator = second_generator_matrix
