class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = Counter(nums)
        for value in dict.values():
            if value > 1:
                return True
            
        return False
        
