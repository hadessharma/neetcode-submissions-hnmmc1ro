class Solution:
    def isValid(self, ch):
        if (
            'A' <= ch <= 'Z' or
            'a' <= ch <= 'z' or
            '0' <= ch <= '9'
        ):
            return True
        
        return False

    
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.isValid(s[l]):
                l += 1
            while l < r and not self.isValid(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True
