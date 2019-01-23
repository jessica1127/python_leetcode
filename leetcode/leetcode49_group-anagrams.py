'''Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''
import itertools

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
       
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]   #a = ['aa'] b=['bb'], a+b = ['aa', 'bb']
        print d.values()
        return d.values()
#下面4个方法没有完全懂，下面要理解：
    def groupAnagrams2(self, strs):
        '''
        :type strs: List[str]
        :rtype: List[List[str]]
        '''
        """
        collections.Counter creates a counter object. A counter object is like a specific kind of dictionary where it is build for counting (objects that hashes to same value)
        tuple(sorted(s)) is used here so that anagrams will be hashed to the same value. tuple is used because sorted returns a list which cannot be hashed but tuples can be hashed
        filter: selects some elements of the list based on given function (first argument - a lambda function is given here)
        lambda function defined here returns True if number of anagrams of that elements is greater than 1
        """
        count = collections.Counter([tuple(sorted(s)) for s in strs])
        return filter(lambda x: count[tuple(sorted(x))]>1, strs)

    def groupAnagrams3(self, strs):
        return [sorted(g) for _, g in itertools.groupby(sorted(strs, key=sorted), sorted)]
      
    def groupAnagrams4(self, strs):
        groups = itertools.groupby(sorted(strs, key=sorted), sorted)
        return [sorted(members) for _, members in groups]

    def groupAnagrams5(self, strs):
        groups = collections.defaultdict(list)
        for s in strs:
            groups[tuple(sorted(s))].append(s)
        return map(sorted, groups.values())
            
        

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    s.groupAnagrams(strs)
            
            
