from typing import Iterable, List, Callable, Set

from generator.first_generator import first_matrix_generator
from algos.algolist import AlgoTypes, ALL_ALGOS
from benchmark.bench import get_execution_time


def test_algos_with_data_generator(data_generator: Callable[[int, int], Iterable[List[int]]],
                                   target_calc: Callable[[int], int],
                                   test_case: List[Set],
                                   debug=False):
    results = {
        AlgoTypes.linear.value: [],
        AlgoTypes.binary.value: [],
        AlgoTypes.exp.value: [],
    }
    m_collection = []
    for m, n in test_case:
        matrix = list(data_generator(m, n))
        m_collection.append(m)
        target = target_calc(n)
        for name, algo in ALL_ALGOS.items():
            exec_time = int(get_execution_time(algo, matrix, target) * 1_000_000)
            results[name.value].append(exec_time)
            if debug:
                print(f"TEST_CASE_1-DATA-1-{name.value}-{exec_time}-{m}-{n}")


    if debug:
        print(results)
    return results, m_collection


if __name__ == "__main__":
    test_algos_with_data_generator(first_matrix_generator, debug=True)
