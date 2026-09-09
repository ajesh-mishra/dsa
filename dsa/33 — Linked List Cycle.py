"""
Time complexity: O(n)
Space complexity: O(1)
"""


class ListNode:
    def __init__(self, val: int = 0, next=None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str | None:
        return str(self.val) if self is not None else None


def create_list(nums: list[int]) -> ListNode | None:
    n: ListNode | None = None
    for v in nums[::-1]:
        ln = ListNode(val=v, next=n)
        n = ln
    return n


def has_cycle(head: ListNode | None) -> bool:
    ...


if __name__ == "__main__":
    ll = create_list([1, 2, 3])
    assert f"{middle_node(ll)}" == "2"

    ll = create_list([1, 2, 3, 4])
    assert f"{middle_node(ll)}" == "3"
