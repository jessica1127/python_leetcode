#/usr/bin/env python
#*-coding utf-8
import collections
'''
refer: https://blog.csdn.net/ayst123/article/details/50460134
Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
'''
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n, self.nth = len(grid), len(grid[0]), -1
        #distance is used to store distance from one point to all the other points
        distance = [[0] * n for _ in xrange(m)]   
        print "distance=", distance
        #buildNumber is a 
        #num==1 is to say it is a building
        #
        buildingNumber = len([
            self.traverse((i, j), m, n, grid, distance)
            for i, row in enumerate(grid)
            for j, num in enumerate(row) if num == 1
        ])

        print "buildingNumber= ", buildingNumber

        return min([
            distance[i][j]
            for i, row in enumerate(grid)
            for j, num in enumerate(row)
            if num == -buildingNumber
        ] or [-1])
    
    def traverse(self, bfsbfs, m, n, grid, distance):
        queue, level, nth = collections.deque([startPoint]), 1, self.nth

        while queue:
            for _ in xrange(len(queue)):
                i, j = queue.popleft()
                print "i=",i,"j=",j

                for x, y in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                    ii, jj = i + x, j + y
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == nth + 1:
                        queue.append((ii, jj))

                        distance[ii][jj] += level
                        grid[ii][jj] = nth
            level += 1

        self.nth -= 1
        
        


if __name__ == '__main__':
    s = Solution()
    grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
    res = s.shortestDistance(grid)
    print res

