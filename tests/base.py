from unittest import TestCase
from typing import Callable, List, Iterable


class BaseAlgoCases:
    class TestsForAllAlgoTests(TestCase):
        algo: Callable[[List[List[int]], int], bool] = None

        def setUp(self) -> None:
            self.matrix1 = [
                [1, 4, 5, 10, 90],
                [3, 10, 11, 12, 102],
                [19, 30, 40, 80, 1000],
                [20, 100, 500, 1000, 10000]
            ]
            self.target1_1 = 80
            self.target1_2 = 5
            self.non_exist_target1_1 = 13
            self.non_exist_target1_2 = 41

        def test_common(self):
            matrix = [
                [1, 2, 3],
                [2, 4, 5],
            ]
            target = 4

            res = self.algo(matrix, target)

            self.assertTrue(res)

        def test_one_element_matrix(self):
            matrix = [[0]]
            target = 0
            self.assertTrue(self.algo(matrix, target))

        def test_no_target_in_matrix(self):
            matrix = [
                [1, 5, 6],
                [3, 6, 10]
            ]
            target = 4
            self.assertFalse(self.algo(matrix, target))

        def test_find_target_in_one_line_matrix(self):
            matrix = [
                [1, 3, 6, 7, 10]
            ]
            target = 7
            self.assertTrue(self.algo(matrix, target))
            non_exist_target = 11
            self.assertFalse(self.algo(matrix, non_exist_target))

        def test_find_target_in_one_row_matrix(self):
            matrix = [
                [1],
                [10],
                [89],
                [101],
                [1000]
            ]
            target = 89
            self.assertTrue(self.algo(matrix, target))
            non_exist_target = 90
            self.assertFalse(self.algo(matrix, non_exist_target))

        def test_algo_on_many_matrix(self):
            self.assertTrue(self.algo(self.matrix1, self.target1_2))
            self.assertTrue(self.algo(self.matrix1, self.target1_1))
            self.assertFalse(self.algo(self.matrix1, self.non_exist_target1_1))
            self.assertFalse(self.algo(self.matrix1, self.non_exist_target1_2))

    class TestsForAllMatrixGenerators(TestCase):
        generator: Callable[[int, int], Iterable[List[int]]]

        def test_common(self):
            matrix = list(self.generator(100, 100))
            self.assertEqual(len(matrix), 100)
            self.assertEqual(len(matrix[0]), 100)

        def test_1(self):
            matrix = list(self.generator(10, 20))
            self.assertEqual(len(matrix), 10)
            self.assertEqual(len(matrix[0]), 20)

