class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        sort=sorted(nums)
        for num in nums:
            ans.append(sort.index(num))
        return ans
