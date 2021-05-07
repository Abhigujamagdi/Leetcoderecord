class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == '':
            return 0
        s1= s.strip(" ").split(" ")
        for char in range(len(s1)-1,-1,-1):
            return len(s1[char])
             
​
