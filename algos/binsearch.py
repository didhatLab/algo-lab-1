from typing import List


def get_target_or_new_column_position(row: List[int], left: int, right: int, target: int):
    while right > left + 1:
        mid = (right + left) // 2
        if row[mid] == target:
            return mid
        elif row[mid] > target:
            right = mid
        elif row[mid] < target:
            left = mid
    return right - 1


def bin_search(matrix: List[List[int]], target_number: int):
    row_index = 0
    column_index = len(matrix[0]) - 1

    while row_index < len(matrix) and column_index >= 0:
        if matrix[row_index][column_index] == target_number:
            return True
        elif matrix[row_index][column_index] < target_number:
            row_index += 1
        elif matrix[row_index][column_index] > target_number:
            column_index = get_target_or_new_column_position(matrix[row_index], 0, column_index, target_number)
    return False
