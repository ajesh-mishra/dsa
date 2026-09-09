"""
Time complexity: O(n * m)
Space complexity: O(n)
The solution works only for lowercase letters
"""

from collections import defaultdict
from typing import DefaultDict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagram_map: DefaultDict[str, list[str]] = defaultdict(list)

    def get_hash(s: str) -> str:
        hash_string = [0 for _ in range(26)]

        for c in s:
            hash_string[ord(c) - 97] += 1

        return "-".join([str(value) for value in hash_string])

    for s in strs:
        h = get_hash(s)
        anagram_map[h].append(s)

    return list(anagram_map.values())


if __name__ == "__main__":
    assert group_anagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"],
    ]
