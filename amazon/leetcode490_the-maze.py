class Solution:
    def hasPath(self, maze, start, destination):
        row = len(maze)
        col = len(maze[0])
        def dfs(x, y, stopped):
            if (x, y) in stopped:
                return False
            stopped.add((x, y))
            if [x, y] == destination:
                return True
            for i, j in [(1, 0),(-1, 0),(0, 1),(0, -1)]:
                tmp_x, tmp_y = x, y
                while 0<= tmp_x+i < row and 0<= tmp_y+j < col and maze[tmp_x+i][tmp_y+j] != 1:
                    tmp_x += i
                    tmp_y += j
                if dfs(tmp_x, tmp_y, stopped):
                    return True
            return False
        return dfs(start[0], start[1], set())





