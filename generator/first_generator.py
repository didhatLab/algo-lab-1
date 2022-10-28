from typing import Iterable, List


def first_matrix_generator(rows_number: int, columns_number: int) -> Iterable[List[int]]:

    for i in range(rows_number):
        row = []
        for j in range(columns_number):
            row.append((columns_number // rows_number * i + j) * 2)
        yield row
