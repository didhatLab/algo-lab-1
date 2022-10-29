from typing import Iterable, List


def second_generator_matrix(rows_number: int, columns_number: int) -> Iterable[List[int]]:

    for i in range(1, rows_number+1):
        row = []
        for j in range(1, columns_number+1):
            row.append((columns_number // rows_number * i * j) * 2)
        yield row


if __name__ == "__main__":

    for x in second_generator_matrix(2, 100):
        print(x)
