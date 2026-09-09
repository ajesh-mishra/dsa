"""
Time complexity: O(n)
Space complexity: O(1)
"""


def character_replacement_not_optimised(s: str, k: int) -> int:
    i = result = 0
    curr_map = [0 for _ in range(26)]

    for j, c in enumerate(s):
        curr_map[ord(c) - 65] += 1

        while sum(curr_map) - max(curr_map) > k and i <= j:
            curr_map[ord(s[i]) - 65] -= 1
            i += 1

        result = max(result, j - i + 1)

    return result


def character_replacement(s: str, k: int) -> int:
    left = 0
    result = 0
    max_frequency = 0
    frequency = [0] * 26

    for right, c in enumerate(s):
        index = ord(c) - ord("A")
        frequency[index] += 1

        max_frequency = max(max_frequency, frequency[index])

        while (right - left + 1) - max_frequency > k:
            frequency[ord(s[left]) - ord("A")] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result


if __name__ == "__main__":
    assert character_replacement(s="ABAB", k=2) == 4
    assert character_replacement(s="AABABBA", k=1) == 4
