"""
Time complexity: O(n)
Space complexity: O(1)
"""


def move_zeroes(nums: list[int]) -> None:
    non_zero_count: int = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            non_zero_count += 1
            nums[non_zero_count - 1] = nums[i]

    for i in range(non_zero_count, len(nums)):
        nums[i] = 0

    return nums


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    assert nums  == [1, 3, 12, 0, 0]
