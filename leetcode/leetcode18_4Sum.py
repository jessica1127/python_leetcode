'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
import itertools

class Solution(object):
    def fourSum(self, num, target):
        def helper(com_res):
            sum = 0
            for i in range(len(com_res)):
                sum += com_res[i]
            return sum
        num.sort()   #need to return in sequence
        comb_restmp = itertools.combinations(num, 4)
        result = []
        for item in comb_restmp:
            if helper(item) == target:
                result.append(item)
        print "result = ",result
        #distinct the result list:
        res = []
        for item in result:
            
            item = list(item)
            print "item= ",item
            if item not in res:
                res.append(item)
        return res
    
    def fourSum2(self, num, target):
        #d is a dict, which key is the twoSum, while value is a list of all two sum item's index
        d = dict()
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                sum2 = num[i] + num[j]
                if sum2 in d:
                    d[sum2].append((i, j))
                else:
                    d[sum2] = [(i, j)]
        print "d= ", d
        result = set()
        for key in d:
            value = target - key  #another twoSum
            if value in d:
                list1 = d[key]
                list2 = d[value]
                for (i, j) in list1:
                    for (k, l) in list2:
                        if i!=k and i!=l and j!=k and j !=l:
                            flist = [num[i], num[j], num[k], num[l]]
                            flist.sort()
                            result.add(tuple(flist))
        return list(result)

    def fourSum3(self, nums, target):
        def dislist(tmplist):
            res = []
            for item in tmplist:
                if item not in res:
                    res.append(item)

            return res

        def comres(nums, tplist):
            res = []
            for i in range(len(tplist)):
                for j in range(i+1, len(tplist)):
                    if i != j:
                        print "tplist[i]= ",tplist[i]
                        print "tplist[j]=",tplist[j]
                        print "tplist[i][0]= ",tplist[i][0]
                        tmp= [nums[tplist[i][0]], nums[tplist[i][1]], nums[tplist[j][0]], nums[tplist[j][1]]]
                        tmp.sort()
                        res.append(tmp)
            print "000 res = ", res           
            return res

        d = dict()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                twoSum = nums[i] + nums[j]
                if twoSum in d:
                    d[twoSum].append((i, j))
                else:
                    d[twoSum] = [(i, j)]
        result = []
        tmpset = set()
        for twoSum, items_list in d.items():
            value = target - twoSum  #the other twoSum
            if value in d:   #that is to say d[value] exists
                items_list2 = d[value]
                itlist = dislist(items_list+items_list2)
                comres = comres(nums, itlist)

        print "comres = ", comres
        return comres

if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    s = Solution()
    result = s.fourSum3(nums, target)
    print "result = ", result
    













