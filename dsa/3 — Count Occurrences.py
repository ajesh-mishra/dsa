"""
Time complexity: O(n)
Space complexity: O(n)
"""
from collections import defaultdict
from typing import DefaultDict


def count_frequency(nums: list[int]) -> dict[int, int]:
    map: DefaultDict[int, int] = defaultdict(int)

    for num in nums:
        map[num] += 1

    return map

if __name__ == "__main__":
    nums = [1, 2, 2, 3, 1, 1, 4]
    assert count_frequency(nums) == {
        1: 3,
        2: 2,
        3: 1,
        4: 1
    }
