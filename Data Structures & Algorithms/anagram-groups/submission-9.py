class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp: dict[tuple[int, ...], set[str]] = {}

        for s in strs:
            freq = [0] * 26

            for ch in s:
                freq[ord(ch) - ord('a')] += 1
            key = tuple(freq)
            if key not in mp:
                mp[key] = set()

            mp[key].add(s)
        
        return [list(x) for x in mp.values()]