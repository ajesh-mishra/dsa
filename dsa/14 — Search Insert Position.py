"""
Time complexity: O(log n)
Space complexity: O(1)
"""


def search_insert(nums: list[int], target: int) -> int:
    start: int = 0
    end: int = len(nums) - 1

    while end - start > 1:
        mid: int = (start + end) // 2

        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            end = mid
        else:
            start = mid + 1

    if target < nums[start]:
        return start
    elif target > nums[end]:
        return end + 1
    else:
        return end


if __name__ == "__main__":
    assert search_insert(nums = [1, 3, 5, 6], target = 5) == 2
    assert search_insert(nums = [1, 3, 5, 6], target = 0) == 0
    assert search_insert(nums = [1, 3, 5, 6],target = 2) == 1
    assert search_insert(nums = [1, 3, 5, 6], target = 7) == 4
