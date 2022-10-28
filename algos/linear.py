from typing import List


def linear_search(matrix: List[List[int]], target_number: int):
    row_index = 0
    column_index = len(matrix[0]) - 1

    while row_index < len(matrix) and column_index >= 0:
        if matrix[row_index][column_index] == target_number:
            return True
        if matrix[row_index][column_index] > target_number:
            column_index -= 1
        elif matrix[row_index][column_index] < target_number:
            row_index += 1
    return False
