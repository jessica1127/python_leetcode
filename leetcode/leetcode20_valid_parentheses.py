class Solution(object):
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