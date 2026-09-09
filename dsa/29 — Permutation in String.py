"""
Time complexity: O(n)
Space complexity: O(1)
"""


def check_inclusion(s1: str, s2: str) -> bool:
    s1_hash = [0] * 26

    for c in s1:
        s1_hash[ord(c) - 97] += 1

    length = len(s1) - 1
    running_hash = [0] * 26

    for index, c in enumerate(s2):
        running_hash[ord(s2[index]) - 97] += 1
        if index < length:
            continue
        if running_hash == s1_hash:
            return True
        running_hash[ord(s2[index - length]) - 97] -= 1

    return False


if __name__ == "__main__":
    assert check_inclusion(s1="ab", s2="eidbaooo") == True
    assert check_inclusion(s1="adc", s2="dcda") == True
    assert check_inclusion(s1="ab", s2="eidboaoo") == False
