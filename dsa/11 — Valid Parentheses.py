"""
Time complexity: O(n)
Space complexity: O(k), k<=n
"""


def is_valid(s: str) -> bool:
    stack_para: list[str] = []

    for c in s:
        if c in ["{", "[", "("]:
            stack_para.append(c)
            continue

        if not stack_para:
            return False

        last_para = stack_para.pop()

        if c == "}" and last_para != "{":
            return False
        if c == "]" and last_para != "[":
            return False
        if c == ")" and last_para != "(":
            return False

    return len(stack_para) == 0


if __name__ == "__main__":
    assert is_valid("([{}])") == True
    assert is_valid("([)]") == False
