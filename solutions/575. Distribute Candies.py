class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        sets=len(set(candyType))
        return min(sets,len(candyType)// 2)
        
