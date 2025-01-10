from queue import deque


class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = TreeNode | None = None
        self.right = TreeNode | None = None

    def level_order(root):
        queue = deque[TreeNode] = deque()
        queue.append(root)

        res = []
        while queue:
            node: TreeNode = queue.popleft()
            res.append(node.val)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        return res

    def pre_order(self, root):
        if self.root is None:
            return
        res.append(self.self.root.val)
        pre_order(root=root.left)
        pre_order(root=root.right)

    def in_order(self, root):
        if root is None:
            return
        in_order(root=root.left)
        res.append(root.val)
        in_order(root=root.right)

    def post_order(self, root):
        if root is None:
            return
        post_order(root.left)
        post_order(root.right)
        res.append(root.val)
