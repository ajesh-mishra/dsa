"""
Time complexity: O(n)
Space complexity: O(1)
"""


def max_area(height: list[int]) -> int:
    left, right, result = 0, len(height) - 1, 0

    while left < right:
        result = max(result, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return result


if __name__ == "__main__":
    assert max_area(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
