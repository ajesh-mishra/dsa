"""
Time complexity: O(n)
Space complexity: O(n)
"""
from collections import defaultdict
from typing import DefaultDict


def first_unique_char(s: str) -> int:
    char_map: DefaultDict[str, int] = defaultdict(int)

    for c in s:
        char_map[c] += 1

    for index, c in enumerate(s):
        if char_map[c] == 1:
            return index

    return -1


if __name__ == "__main__":
    assert first_unique_char("loveleetcode") == 2
