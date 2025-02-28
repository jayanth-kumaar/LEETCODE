# Given an array of strings, find the longest common prefix among them. If there is no common prefix, return an empty string "".
class Solution(object):
    def largestCommonPrefix(self, strs):
        if not strs:
            return ''
        first = min(strs)           #first element in dictionary order
        last = max(strs)           #last element in dictionary order
        order = sorted(strs)
        for i in range(len(first)):
            if first[i] != last[i]:
                return first[:i]
        return first

strs = ["flower","flow","flight"]
obj = Solution()
x = obj.largestCommonPrefix(strs)
print(x)