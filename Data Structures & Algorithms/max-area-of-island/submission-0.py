class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # 1. 越界
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            
            # 2. 遇到水，或者已经访问过的地方
            if grid[r][c] == 0:
                return 0
            
            # 3. 当前格子是陆地，面积先算 1
            grid[r][c] = 0  # 标记为已访问
            
            area = 1
            
            # 4. 向上下左右继续搜索
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            
            return area
        
        max_area = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area