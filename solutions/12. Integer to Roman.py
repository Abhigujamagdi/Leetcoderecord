class Solution:
    def intToRoman(self, num: int) -> str:
        dictionaryInt = {1000 : "M", 900 : "CM",500 : "D", 400 : "CD", 100 : "C", 90 : "XC",                             50 : "L", 40 : "XL", 10 : "X", 9 : "IX", 5 : "V", 4 : "IV", 1 : "I" }
        
        roman = ""
        
        # represent input num in roman number system
        for i, val in dictionaryInt.items():
            
            # update roman string with corresponding roman symbol
            roman += (num // i) * val
            
            # update num as remainder
            num = num % i
        
        
        return roman
