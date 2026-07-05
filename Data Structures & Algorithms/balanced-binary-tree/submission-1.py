class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            if abs(left_height - right_height) > 1:
                return -1

            if left_height == -1 or right_height == -1:
                return -1

            return 1 + max(left_height, right_height)

        return dfs(root) != -1