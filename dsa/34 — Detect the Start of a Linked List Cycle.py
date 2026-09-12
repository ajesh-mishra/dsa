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

    def show(self):
        current = self
        seen = set()

        while current is not None:
            if id(current) in seen:
                print(f"{current.val} → [cycle]")
                return

            seen.add(id(current))
            print(current.val)
            current = current.next


def create_list(nums: list[int]) -> ListNode | None:
    n: ListNode | None = None

    for v in nums[::-1]:
        ln = ListNode(val=v, next=n)
        n = ln

    return n


def create_circular_list(nums: list[int]) -> ListNode | None:
    n: ListNode | None = None
    l: ListNode | None = None
    f: ListNode | None = None

    for i, v in enumerate(nums[::-1]):
        ln = ListNode(val=v, next=n)
        if i == 2:
            l = ln
        if i == 0:
            f = ln
        n = ln

    if f:
        f.next = l

    return n


def detect_cycle(head: ListNode | None) -> ListNode | None:
    slow = fast = head

    while slow is not None and fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow and slow is fast:
            slow = head
            break

    while slow is not None and fast is not None:
        slow = slow.next
        fast = fast.next

        if slow and slow is fast:
            return slow

    return None


if __name__ == "__main__":
    assert detect_cycle(head=create_list([1, 2, 3, 4, 5])) == None
    
    node = detect_cycle(head=create_circular_list([1, 2, 3, 4, 5]))
    assert node is not None
    assert node.val == 3
