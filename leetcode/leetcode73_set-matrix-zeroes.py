"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
Accepted
182,672
Submissions
473,442
Seen this question in a real interview before?
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rowlist = []
        collist = []
        for row, line in enumerate(matrix):
            for col, item in enumerate(line):
                if item == 0:
                    rowlist.append(row)
                    collist.append(col)
                    print "rowlist= ", rowlist, "collist= ",collist
        for i in rowlist:  #update the row
            for col in range(len(matrix[0])):
                matrix[i][col] = 0
        print "matrix= ",matrix

        for j in collist:
            for row in range(len(matrix)):
                matrix[row][j] = 0
        print "222 matrix = ",matrix
        return matrix


        

if __name__ == '__main__':
    input = [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    output = [
      [0,0,0,0],
      [0,4,5,0],
      [0,3,1,0]
    ]
    print "output=", output
    s = Solution()
    if  output == s.setZeroes(input):
        print "Success"
    else:
        print "Fail"
     
