class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp: dict[str, int] = {}

        l: int = 0
        res: int = 0

        for i in range(len(s)):
            if s[i] not in mp:
                mp[s[i]] = 0
            mp[s[i]] += 1

            while i - l + 1 > max(mp.values()) + k:
                mp[s[l]] -= 1
                if mp[s[l]] == 0:
                    del mp[s[l]]
                l += 1
            
            res = max(res, i - l + 1)
        
        return res
