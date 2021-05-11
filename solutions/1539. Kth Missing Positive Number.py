class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        sets=set(arr)
        counter = 0
        for i in range(1,max(sets)):
            if i not in sets:
                counter +=1
                if counter ==k:
                    return i
        return max(sets) + k - counter
        
