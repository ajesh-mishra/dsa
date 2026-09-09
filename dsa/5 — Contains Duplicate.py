"""
Time complexity: O(n)
Space complexity: O(n)
"""

def contains_duplicate(nums: list[int]) -> bool:
    seen: set[int] = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


def contains_duplicate_shortcut(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 4]) == False
    assert contains_duplicate([1, 2, 3, 1, 4]) == True
