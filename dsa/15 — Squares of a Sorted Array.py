"""
Time complexity: O(n)
Space complexity: O(n)
"""


def square_of_sorted_array(nums: list[int]) -> list[int]:
    i: int = 0
    j: int = len(nums) - 1
    result: list[int] = []

    while i <= j:
        double_i = nums[i] * nums[i]
        double_j = nums[j] * nums[j]
        if double_i > double_j:
            result.append(double_i)
            i += 1
        else:
            result.append(double_j)
            j -= 1

    return result[::-1]


if __name__ == "__main__":
    assert square_of_sorted_array(nums=[-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert square_of_sorted_array(nums=[-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
