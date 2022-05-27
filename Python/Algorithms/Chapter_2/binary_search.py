from typing import List


def binary_rec(array: List, start: int, end: int, target: int) -> int:
    if start <= end:
        middle = (start + end) // 2
        if target == array[middle]:
            return middle
        if array[middle] < target:
            return binary_rec(array, middle + 1, end, target)
        else:
            return binary_rec(array, start, middle-1, target)
    return -1


custom_array = [_ for _ in range(100) if _ & 1 == 0]
print(custom_array)
print(binary_rec(custom_array, 0, len(custom_array) - 1, 98))
