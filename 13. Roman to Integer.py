class Solution(object):
    def romanToInt(self, s):
        roman_values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        prev = 0
        total_sum = 0
        for i in s[::-1]:
            if roman_values[i] >= prev:
                total_sum += roman_values[i] 
            else:
                total_sum -= roman_values[i]
            prev = roman_values[i]
        return total_sum


s = 'MCMXCIV'
obj = Solution()
print(obj.romanToInt(s))
