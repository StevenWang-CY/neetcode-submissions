class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            # 越界
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # 水，不处理
            if grid[r][c] == "0":
                return

            # 标记访问过
            grid[r][c] = "0"

            # 四个方向搜索
            dfs(r + 1, c)  # 下
            dfs(r - 1, c)  # 上
            dfs(r, c + 1)  # 右
            dfs(r, c - 1)  # 左


        count = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)

        return count