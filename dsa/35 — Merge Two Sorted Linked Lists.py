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


def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    dummy = ListNode()
    tail = dummy

    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    if list1 is not None:
        tail.next = list1
    else:
        tail.next = list2

    return dummy.next


if __name__ == "__main__":
    head = merge_two_lists(
        list1=create_list([1, 3, 5, 7]), list2=create_list([2, 4, 6, 8])
    )
    if head:
        head.show()
        
    head = merge_two_lists(list1=create_list([1, 3, 5, 7]), list2=None)
    if head:
        head.show()
