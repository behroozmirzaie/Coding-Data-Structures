from typing import List


def binary_search(sorted_list: List, target: int) -> int:
    right = len(sorted_list)
    left = 0
    while left < right:
        middle = (right + left) // 2
        if sorted_list[middle] == target:
            print("I found it")
            return middle
        elif sorted_list[middle] < target:
            left = middle + 1
        else:
            right = middle
    return -1


custom_list = [_ for _ in range(100)]
print(binary_search(custom_list, target=3))
