"""
Time complexity: O(n)
Space complexity: O(n)
"""


def encode(strs: list[str]) -> str:
    result: str = ""

    for word in strs:
        result += f"{len(word)}#{word}"

    return result


def decode(s: str) -> list[str]:
    result: list[str] = []
    i = size = 0

    while i < len(s):
        if s[i].isnumeric():
            size = (size * 10) + int(s[i])
        elif s[i] == "#":
            result.append(s[i + 1 : i + size + 1])
            i += size
            size = 0

        i += 1

    return result


if __name__ == "__main__":
    assert decode(encode(strs=["hello", "world"])) == ["hello", "world"]
    assert decode(encode(strs=["hello", "", "#", "a#b"])) == ["hello", "", "#", "a#b"]
    assert decode(encode(strs=["123", "hello", "", "#", "a#b"])) == [
        "123",
        "hello",
        "",
        "#",
        "a#b",
    ]
