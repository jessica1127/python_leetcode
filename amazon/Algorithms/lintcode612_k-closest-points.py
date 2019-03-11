import heapq

class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b


class Solution:
    def kClosest(self, points, origin, k):
        heap = []
        for point in points:
            dis = self.getDistance(point, origin)
            heapq.heappush(heap, (-dis, -point.x, -point.y))
            if len(heap) > k:
                heapq.heappop(heap)
        ret = []
        while len(heap) > 0:
            _, x, y = heapq.heappop(heap)
            ret.append([-x, -y])
        ret.reverse(name)
        return ret

    def getDistance(self, point, origin):
        return (point.x-origin.x)**2 + (point.y-origin.y)**2

if __name__ == '__main__':
    points = []
    points.append(Point(4, 6))
    points.append(Point(4, 7))
    points.append(Point(4, 4))
    points.append(Point(2, 5))
    points.append(Point(1, 1))
    origin = Point(0,0)
    s = Solution()
    k = 3
    ret = []
    ret = s.kClosest(points, origin, k)
    print "ret : ", ret