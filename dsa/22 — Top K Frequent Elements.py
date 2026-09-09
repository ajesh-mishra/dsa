"""
Time complexity: O(n)
Space complexity: O(n)
This solution fails if there are multiple values repeating for the same frequency.
I could make `result` as lists of lists and handle this.
"""

from collections import defaultdict
from typing import DefaultDict


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    frequency_map: DefaultDict[int, int] = defaultdict(int)

    for num in nums:
        frequency_map[num] += 1

    result: list[int | None] = [None for _ in range(len(nums) + 1)]

    for num, frequency in frequency_map.items():
        result[frequency] = num

    return [value for value in result if value is not None][::-1][:k]


if __name__ == "__main__":
    assert top_k_frequent(nums=[1, 1, 1, 2, 2, 3], k=2) == [1, 2]
    assert top_k_frequent(nums=[1], k=1) == [1]
    assert top_k_frequent(nums=[4, 4, 4, 2, 2, 3, 3, 3, 3], k=2) == [3, 4]
