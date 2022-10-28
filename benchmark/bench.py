import timeit
from typing import Callable, List


def get_execution_time(algo: Callable[[List[List[int]], int], bool], *params):
    return timeit.timeit(lambda: algo(*params), number=100)
