from typing import List


def find_target_or_get_new_column_position(row: List[int], left: int, right: int, target: int):
    while right >= left:
        mid = (right + left) // 2
        if row[mid] == target:
            return mid
        elif row[mid] > target:
            right = mid - 1
        elif row[mid] < target:
            left = mid + 1
    return right


def find_bounds_for_bin(row: List[int], left: int, right: int, target: int) -> [int, int]:
    bound = 1

    while right >= bound and row[left + bound] < target:
        bound *= 2
    # bound >>= 1
    return bound // 2, min(bound, right)


def exp_search(matrix: List[List[int]], target: int):
    row_index = 0
    column_index = len(matrix[0]) - 1

    while row_index < len(matrix) and column_index >= 0:
        if matrix[row_index][column_index] == target:
            return True

        elif matrix[row_index][column_index] < target:
            row_index += 1

        elif matrix[row_index][column_index] > target:
            left, right = find_bounds_for_bin(matrix[row_index], 0, column_index, target)

            column_index = find_target_or_get_new_column_position(matrix[row_index], left, right, target)
    return False
