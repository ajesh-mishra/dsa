"""
Time complexity: O(n)
Space complexity: O(n)
"""


def second_largest(nums: list[int]) -> int:
    largest, second_largest = (nums[0], nums[1]) if nums[0] > nums[1] else (nums[1], nums[0])

    for num in nums[2:]:
        if num == largest:
            continue
        elif num > largest:
            second_largest, largest = largest, num
        elif num > second_largest:
            second_largest = num

    return second_largest


def second_largest_no(nums: list[int]) -> int:
    new_nums: list[int] = list(set(nums))

    for j in range(2):
        for i in range(1, len(new_nums) - j):
            if new_nums[i] < new_nums[i - 1]:
                new_nums[i], new_nums[i - 1] = new_nums[i - 1], new_nums[i]

    return new_nums[-2]


if __name__ == "__main__":
    nums = [10, 5, 8, 10, 3, 8]
    assert second_largest(nums) == 8
