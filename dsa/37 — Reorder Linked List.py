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
        current, seen = self, set()

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


def reorder_linked_list(head: ListNode | None) -> ListNode | None:
    # Find the middle
    slow = fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    head2 = None
    if slow:
        head2 = slow.next
        slow.next = None

    # Reverse a linked list
    rev_head = None
    while head2:
        n = head2.next
        head2.next = rev_head
        rev_head = head2
        head2 = n

    # Merge/rearrange two lists
    dummy = ListNode()
    tail = dummy
    while head and rev_head:
        tail.next = head
        head = head.next
        tail.next.next = rev_head
        tail = tail.next.next
        rev_head = rev_head.next

    if head and tail:
        tail.next = head

    return dummy.next


if __name__ == "__main__":
    head = reorder_linked_list(head=create_list([1, 2, 3, 4]))
    print("Linked List:")
    if head:
        head.show()

    head = reorder_linked_list(head=create_list([1, 2, 3, 4, 5]))
    print("Linked List:")
    if head:
        head.show()
