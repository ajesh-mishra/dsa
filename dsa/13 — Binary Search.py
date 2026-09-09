"""
Time complexity: O(n)
Space complexity: O(1)
"""


def binary_search(nums: list[int], target: int) -> int:
    start = 0
    end = len(nums) - 1

    while start < end:
        mid = (start + end) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


if __name__ == "__main__":
    assert binary_search(nums = [1, 3, 5, 7, 9, 11], target = 7) == 3
    assert binary_search(nums = [1, 3, 5, 7, 9, 11], target = 4) == -1
    assert binary_search(nums = [1, 3, 5, 7, 11], target = 4) == -1

