"""
Time complexity: O(n)
Space complexity: O(1)
"""


class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next

    def show(self):
        print(self.val)
        if self.next is not None:
            self.next.show()


def create_list(nums: list[int]) -> ListNode | None:
    n: ListNode | None = None
    for v in nums[::-1]:
        ln = ListNode(val=v, next=n)
        n = ln
    return n


def reverse_list(head: ListNode | None) -> ListNode | None:
    prev: ListNode | None = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


if __name__ == "__main__":
    print(f"\nOriginal List: ")
    ll = create_list([1, 2, 3])
    if ll is not None:
        ll.show()

    print("\nReversed List: ")
    ll = reverse_list(ll)
    if ll is not None:
        ll.show()
