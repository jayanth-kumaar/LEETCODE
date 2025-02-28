# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Can you come up with an algorithm that is less than O(n2) time complexity?
class Solution(object):
    def TwoSum(self,x,target):
        pastValues = {}
        for i,v in enumerate(x):
            if (target - v) in pastValues:
                return [pastValues[target-v],i]
            pastValues[v] = i

obj = Solution()
x = [1,7,4,17,9,54,5]
target = 9
print('indexs :', obj.TwoSum(x,target))
