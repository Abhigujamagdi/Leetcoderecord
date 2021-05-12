class Solution:
    def reverseWords(self, s: str) -> str:
        string=s.split(' ')
        res=[]
        for i in string:
            rev = i[::-1]
            res.append(rev)
        return ' '.join(res)
