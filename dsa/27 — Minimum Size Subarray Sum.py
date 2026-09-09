"""
Time complexity: O(n)
Space complexity: O(1)
"""


def min_sub_array_len(target: int, nums: list[int]) -> int:
    left = 0
    curr_sum = 0
    result = float("inf")

    for right, num in enumerate(nums):
        curr_sum += num

        while curr_sum >= target:
            result = min(result, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    return 0 if result == float("inf") else int(result)


if __name__ == "__main__":
    assert min_sub_array_len(nums=[2, 3, 1, 2, 4, 3], target=7) == 2
    assert min_sub_array_len(nums=[1, 4, 4], target=4) == 1
    assert min_sub_array_len(nums=[1, 1, 1, 1, 1], target=11) == 0
