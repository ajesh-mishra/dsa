from collections import deque


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left=None,
        right=None,
    ):
        self.val = val
        self.left = left
        self.right = right


def create_tree(values: list[int | None]) -> TreeNode | None:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def show_tree(root: TreeNode | None) -> None:
    if root is None:
        print("<empty tree>")
        return

    def show(node: TreeNode | None, prefix: str, is_left: bool) -> None:
        if node is None:
            return

        print(prefix + ("├── " if is_left else "└── ") + str(node.val))

        children_prefix = prefix + ("│   " if is_left else "    ")

        if node.left is not None or node.right is not None:
            show(node.left, children_prefix, True)
            show(node.right, children_prefix, False)

    print(root.val)
    show(root.left, "", True)
    show(root.right, "", False)


def max_depth_bfs(root: TreeNode | None) -> int:
    if root is None:
        return 0

    queue = deque()
    queue.append((root, 1))

    while queue:
        node, depth = queue.popleft()
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return depth


def max_depth_dfs(root: TreeNode | None) -> int:
    result: int = 0

    def dfs(node: TreeNode | None, depth: int) -> None:
        nonlocal result

        if node is None:
            result = max(result, depth)
            return None

        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 0)
    return result

def max_depth(root: TreeNode | None) -> int:
    if root is None:
        return 0

    return 1 + max(
        max_depth(root.left),
        max_depth(root.right),
    )


if __name__ == "__main__":
    root = create_tree([3, 9, 20, None, None, 15, 7])
    show_tree(root)
    assert max_depth(root) == 3

    root = create_tree([1, None, 2, None, 3, None, 4])
    show_tree(root)
    assert max_depth(root) == 4
