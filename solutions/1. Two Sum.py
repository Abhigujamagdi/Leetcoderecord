class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i,n in enumerate(nums):
            number = target - n
            if number in dict:
                return [dict[number],i]
            dict[n] = i
        return []
            
