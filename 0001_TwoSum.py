class Solution:
    def twoSum(self, nums, target):
        checked = {}
        #looping through the nums as a dictionary
        for i, num in enumerate(nums):
            #getting the complement of each values and comparing it with what is in the dict
            complement = target - num
            if complement in checked:
                return [checked[complement], i]
            #switched num and i; easy to get index
            checked[num] = i
