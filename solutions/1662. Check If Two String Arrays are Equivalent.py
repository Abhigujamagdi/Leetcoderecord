class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string1=''
        string2=''
        for i in word1:
            string1 +=str(i) 
        
        for j in word2:
            string2 +=str(j)
        
        if string1 == string2:
            return True
        
            
