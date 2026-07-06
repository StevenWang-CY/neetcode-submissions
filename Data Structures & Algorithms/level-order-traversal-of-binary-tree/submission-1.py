class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        stack = [(root, 0)]
        result = []

        while stack:
            node, level = stack.pop()

            if level == len(result):
                result.append([])

            result[level].append(node.val)

            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))

        return result