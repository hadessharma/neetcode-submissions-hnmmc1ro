class Solution:
    def minWindow(self, s: str, t: str) -> str:
        to_find: int = 0
        min_l, min_r = 0, 0
        res = float("inf")
        
        if len(t) > len(s):
            return ""
        mp_t: dict[str, int] = defaultdict(int)

        for i in range(len(t)):
            mp_t[t[i]] += 1
        
        l: int = 0
        to_find = len(mp_t)
        
        mp_s: dict[str, int] = defaultdict(int)

        for i in range(len(s)):            
            mp_s[s[i]] += 1    
            
            if mp_s[s[i]] == mp_t[s[i]]:
                to_find -= 1

            while to_find == 0:
                if i - l + 1 < res:
                    res = i - l + 1
                    min_l = l
                    min_r = i + 1
                if mp_s[s[l]] == mp_t[s[l]]:
                    to_find += 1
                
                mp_s[s[l]] -= 1
                l += 1
        
        if to_find == 0:
            res = min(res, len(s) - l)
        
        return s[min_l: min_r]
