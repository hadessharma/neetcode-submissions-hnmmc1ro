class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            l = len(s)
            res.append(str(l) + "#" + s)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        l = 0
        res = []
        print(s)
        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1
            
            print(l, r)
            s_len = int(s[l:r])
            l = r + 1

            res.append(s[l: l + s_len])
            print(res)
            l = l + s_len

        return res


