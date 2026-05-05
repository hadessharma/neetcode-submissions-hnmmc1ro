class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_arr: list[int] = [0] * 26

        for i in range(len(s)):
            freq_arr[ord(s[i]) - ord('a')] += 1
            freq_arr[ord(t[i]) - ord('a')] -= 1
        
        for n in freq_arr:
            if n != 0:
                return False
        
        return True