from typing import List


def find_new_column_position(row: List[int], left: int, right: int, target: int):
    ans = -1
    while left <= right:
        mid = (right + left) // 2
        if row[mid] <= target:
            left = mid + 1
            ans = mid
        else:
            right = mid - 1

    return ans


def get_exp_bound(matrix, row_index, column_index: int, target: int):
    if column_index > 16:
        exp = 2
        while column_index >= exp and matrix[row_index][column_index - exp] > target:
            exp <<= 1
        exp >>= 1
    else:
        exp = 0

    return exp


def exp_search(matrix: List[List[int]], target: int):
    row_index = 0
    column_index = len(matrix[0]) - 1

    while row_index < len(matrix) and column_index > -1:
        if matrix[row_index][column_index] == target:
            return True
        elif matrix[row_index][column_index] < target:
            row_index += 1
        else:
            exp = get_exp_bound(matrix, row_index, column_index, target)

            column_index = find_new_column_position(matrix[row_index],
                                                    0,
                                                    column_index - exp,
                                                    target)
    return False
