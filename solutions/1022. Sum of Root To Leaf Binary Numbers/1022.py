def sum_root_to_leaf(root) -> int:
    if not root:
        return 0

    total = 0
    stack = [(root, 0)]

    while stack:
        node, current = stack.pop()
        current = (current << 1) | node.val

        if not node.left and not node.right:
            total += current
        else:
            if node.right:
                stack.append((node.right, current))
            if node.left:
                stack.append((node.left, current))

    return total
