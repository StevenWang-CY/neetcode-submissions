from collections import deque


class Solution:
    def islandsAndTreasure(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        # 四个方向
        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]


        # 1. 所有宝藏入队
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))


        # 2. BFS
        while q:

            r,c = q.popleft()


            for dr,dc in directions:

                nr = r + dr
                nc = c + dc


                # 越界
                if nr < 0 or nr >= rows:
                    continue

                if nc < 0 or nc >= cols:
                    continue


                # 水不能走
                if grid[nr][nc] == -1:
                    continue


                # 已经访问
                if grid[nr][nc] != 2147483647:
                    continue


                # 更新距离
                grid[nr][nc] = grid[r][c] + 1

                q.append((nr,nc))