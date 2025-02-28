# Given an integer x, return true if x is a palindrome, and false otherwise.
# Could you solve it without converting the integer to a string?

class Solution(object):
    def palindromeNum(self,x):
        original = x
        reverse = 0
        while x > 0:
            reverse = (reverse*10) + (x%10)
            x = x//10
        return reverse == original
x = 121
obj = Solution()
print(obj.palindromeNum(x))

for i in [121,343,456,654,767,89098]:
    print(i,obj.palindromeNum(i))