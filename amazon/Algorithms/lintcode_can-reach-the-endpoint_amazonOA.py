#-*-coding: utf-8
'''
给一个大小为 m*n 的map，1 代表空地，0 代表障碍物，9代表终点。请问如果你从 (0, 0) 开始能否到达终点？

在线评测地址: http://www.lintcode.com/problem/can-reach-the-endpoint/
'''
import Queue

class Solution(object):
    def reachEndpoint(self, map):
        n = len(map)
        m = len(map[0])
        if n ==0 or m ==0:
            return False
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        vis =  [[False for i in range(m)] for j in range(n)]
        q = Queue.Queue()
        q.put(0)
        while not q.empty():
            cur = q.get()
            print "cur = ", cur
            curx = cur / m
            cury = cur % m
            print "curx = ", curx, "cury = ",cury
            for i in range(4):
                nx = curx + dx[i]
                ny = cury + dy[i]
                if nx < 0 or nx >= n or ny<0 or ny >= m or vis[nx][ny] or map[nx][ny] == 0:
                    continue
                if map[nx][ny] == 9:
                    return True
                q.put(nx * m + ny)
                vis[nx][ny] = True
        return False

    def reachEndPoint2(self, map):
        '''
        n * m 
        '''
        n = len(map)
        m = len(map[0])
        if m ==0 or n == 0:
            return False
        q = Queue.Queue()
        q.put(0)
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        vis = [[False for i in range(m)] for j in range(n)]
        while not q.empty():
            cur = q.get()
            curx = cur / m
            cury = cur % m
            for i in range(4):
                nx = curx + dx[i]
                ny = cury + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m or vis[nx][ny] == True or map[nx][ny] == 0:
                    continue
                if map[nx][ny] == 9:
                    return True
                q.put(nx * m + ny)
                vis[nx][ny] = True
        OA2019return False




        
s = Solution()
map = [[1, 1, 1, 1],
       [0, 1, 1, 0],
       [1, 1, 9, 1]]
print s.reachEndPoint2(map)

