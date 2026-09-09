"""
Time complexity: O(n)
Space complexity: O(n)
"""


def longest_consecutive(nums: list[int]) -> int:
    result, nums = 0, set(nums)

    for num in nums:
        if num - 1 in nums:
            continue

        temp_result, next = 1, num + 1

        while next in nums:
            temp_result += 1
            next += 1

        result = max(result, temp_result)

    return result


if __name__ == "__main__":
    assert longest_consecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive(nums=[100, 4, 200, 1, 3, 2]) == 4
