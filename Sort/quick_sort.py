class Solution:
    def sortInteger2(self, A):
        print "before sort==", A
        self.quick_sort(A, 0, len(A)-1)
        print "after sort==", A



    def quick_sort(self, A, start, end):
        if start >= end:
            return
        left, right = start, end
        pivot = A[(start+end)//2]
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        self.quick_sort(A, start, left)
        self.quick_sort(A, left, end)




if __name__ == '__main__':
    A = [8, 0, 2, 5, 7]
    s = Solution()
    s.sortInteger2(A)
