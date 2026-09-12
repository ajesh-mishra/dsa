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


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    dummy = ListNode(next=head)

    slow = fast = dummy

    for _ in range(n):
        if fast is None:
            return head
        fast = fast.next

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next

    if slow and slow.next:
        slow.next = slow.next.next

    return dummy.next


if __name__ == "__main__":
    print(f"Linked List:")
    head = remove_nth_from_end(head=create_list([1, 2, 3, 4, 5]), n=2)
    if head:
        head.show()

    print(f"Linked List:")
    head = remove_nth_from_end(
        head=create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, -1, 8]), n=4
    )
    if head:
        head.show()

    print(f"Linked List:")
    head = remove_nth_from_end(head=create_list([1, 2]), n=1)
    if head:
        head.show()

    print(f"Linked List:")
    head = remove_nth_from_end(head=create_list([1, 2]), n=10)
    if head:
        head.show()
