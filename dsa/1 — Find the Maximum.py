"""
Time complexity: O(n)
Space complexity: O(1)
"""

def find_max(nums: list[int]) -> int | None:
    if not nums:
        return None

    max = nums[0]

    for num in nums:
        if num > max:
            max = num

    return max


if __name__ == "__main__":
    nums = [4, 7, 1, 9, 3]
    assert find_max(nums) == 9
