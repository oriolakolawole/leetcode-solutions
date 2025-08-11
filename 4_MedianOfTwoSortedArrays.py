import math

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # using the smallest array for partitioning
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        
        low , high = 0, m
        while low <= high:
            # getting the position for partitioning
            nums1Part = (low + high) // 2 
            nums2Part = math.ceil((m + n) / 2) - nums1Part
            
            # spliting each list into two havles, getting the max of the left partition of both array 
            # getting the mix of the right partition of both array
            leftMax1 = float(nums1[nums1Part - 1]) if nums1Part > 0 else float('-inf')
            rightMin1 = float(nums1[nums1Part]) if nums1Part < m else float('inf')
            leftMax2 = float(nums2[nums2Part - 1]) if nums2Part > 0 else float('-inf')
            rightMin2 = float(nums2[nums2Part]) if nums2Part < n else float('inf')
            
            # returning the median 
            if leftMax1 <= rightMin2 and leftMax2 <= rightMin1:
                if (m + n) % 2 == 0:
                    return (max(leftMax1, leftMax2) + min(rightMin1, rightMin2)) / 2
                return max(leftMax1, leftMax2)
            
            # shifting right if the partition is not balanced
            elif leftMax2 > rightMin1:
                low = nums1Part + 1
            
            # shifting left 
            else:
                high = nums1Part - 1
            
