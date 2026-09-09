"""
Sort Time complexity: O(n log n)
Time complexity: O(n)
Space complexity: O(n)
"""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    result: list[list[int]] = []

    for interval in sorted(intervals, key=lambda x: x[0]):
        if result and interval[1] <= result[-1][1]:
            continue

        if result and interval[0] <= result[-1][1]:
            result[-1][1] = interval[1]
            continue

        result.append(interval)

    return result


if __name__ == "__main__":
    assert merge(intervals=[[1, 10], [2, 3], [4, 5], [6, 7]]) == [[1, 10]]
    assert merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6],
        [8, 10],
        [15, 18],
    ]
    assert merge(intervals=[[1, 4], [4, 5]]) == [[1, 5]]
