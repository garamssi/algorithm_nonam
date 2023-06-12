from collections import deque


def bfs(root):
    visited = []

    if root is None:
        return []

    q = deque()
    q.append(root)

    while q:
        cur_node = q.popleft()
        visited.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


bfs(Node(1, 2, 3))
