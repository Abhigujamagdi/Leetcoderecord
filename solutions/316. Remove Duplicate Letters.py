class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dictionary = {char: indx for indx, char in enumerate(s)}
        
        result = []
        
        for index, char in enumerate(s):
            if char not in result:
                
                while result and index < dictionary[result[-1]] and char < result[-1]:
                    result.pop()
                    
                result.append(char)
        
        return "".join(result)
