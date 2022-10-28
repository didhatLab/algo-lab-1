from unittest import TestCase
from tests.base import BaseAlgoCases
from algos.binsearch import bin_search


class TestSearch(BaseAlgoCases.TestsForAllAlgoTests):

    def setUp(self) -> None:
        super().setUp()
        self.algo = bin_search
