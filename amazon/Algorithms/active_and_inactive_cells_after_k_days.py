'''
Reference:https://www.geeksforgeeks.org/active-inactive-cells-k-days/
'''
class Solution:
    def activeAndInactive(self, cells, n, k): 
        #cells: store current status of cells 
        #n : number of cells
        #k : after k days
        # tmp is used to store cells
        tmp = []
        for i in range(n+1):
            tmp.append(False)
        for i in range(n):
            tmp[i] = cells[i]
        print "original cells = ", cells
        print "original tmp = ", tmp
        #Iterator for k days:
        while(k > 0):
            #corner case
            tmp[0] = False ^ cells[1]
            tmp[n-1] = False ^ cells[n-2]

            for i in range(1, n-1):
                tmp[i] = cells[i-1] ^ cells[i+1]

            for i in range(0, n):
                cells[i] = tmp[i]
            k -= 1

        active = 0
        inactive = 0
        for i in range(n):
            if cells[i] == True:
                active += 1
            else:
                inactive += 1
        print("Active Cells =",active," , ", "Inactive Cells =", inactive)
        return active, inactive

if __name__ == '__main__':
    cells = [False, True, False, True, 
         False, True, False, True] 
    k = 3
    n =len(cells) 
    s = Solution()
    active, inactive = s.activeAndInactive(cells, n, k)
    print "000 active = ", active, " \ninactive= ", inactive
