class Solution(object):
    def isValid(self, s):
        pair = {'(':')','[':']','{':'}'}
        stack = []
        for i in s:
            if i in pair:
                stack.append(i)
            elif i in pair.values():
                if not stack or i != pair[stack.pop()]:
                    return False
        return not stack

        
s = '(we){(df""}'
s1 = '(we){(df"")}'
   
obj = Solution()
print(obj.isValid(s))
print(obj.isValid(s1))
        