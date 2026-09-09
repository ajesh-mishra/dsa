"""
Time complexity: O(n2)
Space complexity: O(1)
"""


def longest_palindrome(s: str) -> str:
    result_left = result_right = 0

    def check_around(left: int, right: int) -> None:
        nonlocal result_left
        nonlocal result_right

        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left > result_right - result_left:
                result_right, result_left = right, left
            left -= 1
            right += 1

    for i in range(len(s)):
        check_around(i, i + 1)
        check_around(i - 1, i + 1)

    return s[result_left : result_right + 1]


if __name__ == "__main__":
    assert longest_palindrome(s="babad") == "bab"
    assert longest_palindrome(s="cbbd") == "bb"
    assert longest_palindrome(s="a") == "a"
    assert longest_palindrome(s="ac") == "a"
