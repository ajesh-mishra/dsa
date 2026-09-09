"""
Time complexity: O(n2)
Space complexity: O(n)
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    result: list[list[int]] = []

    for index, num in enumerate(nums):
        if index > 0 and num == nums[index - 1]:
            continue

        target, left, right = -1 * num, index + 1, len(nums) - 1

        while left < right:
            total: int = nums[left] + nums[right]
            if total == target:
                result.append([num, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1

    return result


if __name__ == "__main__":
    assert three_sum(nums=[-1, 0, 1, 2, -1, -4]) == [
        [-1, -1, 2],
        [-1, 0, 1]
    ]
    assert three_sum(nums=[0, 1, 1]) == []
    assert three_sum(nums=[0, 0, 0, 0]) == [
        [0, 0, 0]
    ]
