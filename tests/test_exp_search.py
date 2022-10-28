from tests.base import BaseAlgoCases
from algos.exp import exp_search


class TestExpSearch(BaseAlgoCases.TestsForAllAlgoTests):

    def setUp(self) -> None:
        super(TestExpSearch, self).setUp()
        self.algo = exp_search
