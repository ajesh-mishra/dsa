"""
Time complexity: O(n)
Space complexity: O(k), k<=n
"""

from collections import defaultdict
from typing import DefaultDict


def longest_k_distinct(s: str, k: int) -> int:
    i = j = result = 0
    curr_map: DefaultDict[str, int] = defaultdict(int)

    while j < len(s):
        curr_map[s[j]] += 1

        while len(curr_map) > k:
            curr_map[s[i]] -= 1
            if curr_map[s[i]] == 0:
                del curr_map[s[i]]
            i += 1

        result = max(result, j - i + 1)
        j += 1

    return result


if __name__ == "__main__":
    assert longest_k_distinct(s="eceba", k=2) == 3
    assert longest_k_distinct(s="aa", k=1) == 2
    assert longest_k_distinct(s="aabbcc", k=2) == 4
    assert longest_k_distinct(s="abc", k=0) == 0
