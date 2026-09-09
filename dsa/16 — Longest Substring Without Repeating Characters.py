"""
Time complexity: O(2n) ~ O(n)
Space complexity: O(k), k<=n
"""


def longest_unique_substring(s: str) -> int:
    left, right, result, seen = 0, 0, 0, set()

    while right < len(s):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        result = max(result, right - left + 1)
        right += 1

    return result


if __name__ == "__main__":
    assert longest_unique_substring(s="abcabcbb") == 3
    assert longest_unique_substring(s="pwwkew") == 3
    assert longest_unique_substring(s="bbbbbb") == 1
