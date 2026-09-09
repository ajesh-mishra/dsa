"""
Time complexity: O(n)
Space complexity: O(1)
"""


def remove_duplicates(nums: list[int]) -> int:
    next_unique_position: int = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[next_unique_position]:
            next_unique_position += 1
            nums[next_unique_position] = nums[i]

    return next_unique_position + 1


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(nums)
    assert nums[:k] == [0, 1, 2, 3, 4]
