class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row,col=len(grid),len(grid[0])
        island=0

        def bfs(r,c):
            q=collections.deque()
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            q.append((r,c))
            grid[r][c]="0"
            while q:
                nr,nc=q.popleft()
                for dr,dc in directions:
                    r,c=nr+dr,nc+dc
                    if (r in range(row) and c in range(col) and grid[r][c]=="1"):
                        q.append((r,c))
                        grid[r][c]="0"
        for r in range (row):
            for c in range (col):
                if grid[r][c]=="1":
                    bfs(r,c)
                    island+=1
        return island
