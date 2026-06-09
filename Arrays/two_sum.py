class Solution(object):
    def twoSum(self, nums, target):
        s={}
        for i in range(len(nums)):
            n=nums[i]
            c=target-n
            if c in s:
                return [s[c],i]
            s[n]=i