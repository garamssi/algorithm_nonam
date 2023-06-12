# Postorder 기본
def lca(root, p, q):

    if root is None:
        return None

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if root == p or root == q:
        return root
    elif left and right:
        return root
    return left or right


lca([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 6, 4)