class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        stc = sentence.split(' ')
        for i in stc:
            if searchWord == i[:len(searchWord)]:
                return stc.index(i)+1
        return -1
        
        
        
