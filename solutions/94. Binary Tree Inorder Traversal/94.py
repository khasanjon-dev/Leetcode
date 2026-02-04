def inorder_traversal(root) -> list[int]:
    result = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

    dfs(root)
    return result


print(inorder_traversal([1, None, 2, 3]))
