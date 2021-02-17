class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i,j in enumerate(nums):
            if j not in nums[i+1:] and j not in nums[:i]:
                return j
        
