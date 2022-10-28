from tests.base import BaseAlgoCases
from algos.linear import linear_search


class TestLinearSearch(BaseAlgoCases.TestsForAllAlgoTests):

    def setUp(self) -> None:
        super().setUp()
        self.algo = linear_search
