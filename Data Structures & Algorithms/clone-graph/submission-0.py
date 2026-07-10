class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        oldToNew = {}

        def dfs(node):
            # 已经复制
            if node in oldToNew:
                return oldToNew[node]

            # 创建新节点
            copy = Node(node.val)

            # 保存映射
            oldToNew[node] = copy

            # 复制邻居
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)