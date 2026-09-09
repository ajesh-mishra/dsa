"""
Time complexity: O(n)
Space complexity: O(n)
"""


def product_except_self(nums: list[int]) -> list[int]:
    prefix = []
    running_product = 1

    for num in nums:
        prefix.append(running_product)
        running_product *= num

    suffix = []
    running_product = 1

    for num in nums[::-1]:
        suffix.append(running_product)
        running_product *= num

    return [p * s for p, s in zip(prefix, suffix[::-1])]


def product_except_self_optimised(nums: list[int]) -> list[int]:
    result = []
    running_product = 1

    for num in nums:
        result.append(running_product)
        running_product *= num

    running_product = 1

    for i in range(len(nums) - 1, -1, -1):
        result[i] *= running_product
        running_product *= nums[i]

    return result


if __name__ == "__main__":
    assert product_except_self(nums=[1, 2, 3, 4]) == [24, 12, 8, 6]
