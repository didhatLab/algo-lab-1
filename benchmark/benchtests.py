from typing import Iterable, List, Callable

from generator.first_generator import first_matrix_generator
from algos.algolist import AlgoTypes, ALL_ALGOS
from benchmark.bench import get_execution_time


def test_algos_with_data_generator(data_generator: Callable[[int, int], Iterable[List[int]]],
                                   debug=False):
    results = {
        AlgoTypes.linear.value: [],
        AlgoTypes.binary.value: [],
        AlgoTypes.exp.value: [],
    }
    m, n = 1, 100_000
    m_collection = []
    while n > 0:
        matrix = list(data_generator(m, n))
        m_collection.append(m)
        target = 2 * n + 1
        for name, algo in ALL_ALGOS.items():
            exec_time = get_execution_time(algo, matrix, target)
            results[name.value].append(exec_time)
            if debug:
                print(f"{name.value}-{exec_time}-{m}-{n}")

        m *= 10
        n //= 10
    if debug:
        print(results)
    return results, m_collection


if __name__ == "__main__":
    test_algos_with_data_generator(first_matrix_generator, debug=True)

