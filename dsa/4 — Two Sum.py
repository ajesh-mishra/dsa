"""
Time complexity: O(n)
Space complexity: O(n)
"""
from collections import defaultdict
from typing import DefaultDict


def two_sum(nums: list[int], target: int) -> list[int]:
    sum_map: DefaultDict[int, int] = defaultdict(int)

    for index, num in enumerate(nums):
        if (i := sum_map.get(num)) is not None:
            return [i, index]

        sum_map[target - num] = index


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    assert two_sum(nums, target) == [0, 1]
