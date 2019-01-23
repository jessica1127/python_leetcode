class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        res = []
        def helper(digits):
            # define a dictionary of the character <-> number projection
            pad = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
            # if the input is empty
            print "len(digits)= ",len(digits)
        
            if len(digits) == 0:
                print "000"
                return [""]
            
            # for number string length equals n-1    
            print "digits= ",digits
            d0 = digits[:-1]
            comb0 = self.letterCombinations(d0)
            print "d0= ",d0, "comb0 = ", comb0
            # combine the last digit with previous n-1 string
            d1 = digits[-1]
            string1 = pad[d1]
            comb1 = []
            #  consider every combinations
            for s in string1:
                if len(comb0) != 0:
                    for c in comb0:
                        cs = c+s
                        comb1.append(cs)
                else:
                    comb1.append(s)
            return comb1
        if len(digits) == 0:
            return res
        else:
            return helper(digits)

        
                
        
        
if __name__ == '__main__':
    digits = "23"
    s = Solution()
    res = s.letterCombinations(digits)
    print "res = ", res
    digits1 = ""
    res1 = s.letterCombinations(digits1)
    print "res1 = ", res1
   