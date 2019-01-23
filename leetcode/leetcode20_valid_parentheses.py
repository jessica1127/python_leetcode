class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {"}":"{","]":"[",")":"("}
        tmpstack = []
        for char in s:
            print "000char = ",char
            if char in dict.values():
                print "char=",char
                tmpstack.append(char)
            elif char in dict.keys():
                print "111char =", char
                print "dict[char] =", dict[char]
                if tmpstack != [] and tmpstack.pop() == dict[char]:
                    print "222char=",char
                    return True
                else:
                    return False
            else:
                return False
        return len(tmpstack) == 0
    def isValid2(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            print "000 char=",char
            if char in dict.values():
                stack.append(char)
                print "stack= ",stack
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
                

if __name__ == '__main__':
    input = "(]"
    s = Solution()
    res = s.isValid2(input)
    print "res=",res