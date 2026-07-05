class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            self.diameter = max(self.diameter, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)

        dfs(root)
        return self.diameter