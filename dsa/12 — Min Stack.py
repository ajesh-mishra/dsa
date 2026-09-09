"""
Time complexity: O(n)
Space complexity: O(n)
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.track_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.track_min or val < self.track_min[-1]:
            self.track_min.append(val)
        else:
            self.track_min.append(self.track_min[-1])

    def pop(self) -> None:
        self.track_min.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.track_min[-1]

