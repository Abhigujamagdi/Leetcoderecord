class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        string,ans = {},""
        
        for i,j in zip (s,indices):
            string[j] = i
            
        for i in range (len(string)):
            ans+= string[i]
            
        return ans
        
