from typing import Iterable, List


def first_matrix_generator(rows_number: int, columns_number: int) -> Iterable[List[int]]:

    for i in range(1, rows_number+1):
        row = []
        for j in range(1, columns_number+1):
            row.append((columns_number // rows_number * i + j) * 2)
        yield row


if __name__ == "__main__":

    for k in first_matrix_generator(100, 100):
        print(k)