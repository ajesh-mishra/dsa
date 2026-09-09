"""
Time complexity: O(n)
Space complexity: O(n)
"""
from collections import defaultdict
from typing import DefaultDict


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    letter_map: DefaultDict[int, int] = defaultdict(int)

    for c in s:
        letter_map[c] += 1

    for c in t:
        if letter_map[c] < 1:
            return False
        letter_map[c] -= 1

    return all([v == 0 for v in letter_map.values()])


if __name__ == "__main__":
    assert is_anagram("listen", "silent") == True
    assert is_anagram("listen", "silen") == False
