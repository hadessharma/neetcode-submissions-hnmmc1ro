class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp = [[] for _ in range(len(nums) + 2)]

        mp_ele_freq = defaultdict(int)

        for n in nums:
            mp_ele_freq[n] += 1
        
        mp_freq_eles = defaultdict(list)

        for key, val in mp_ele_freq.items():
            mp[val].append(key)
        
        print(mp)
        res = []
        for i in range(len(nums) + 1, 0, -1):
            print(i)
            for ele in mp[i]:
                res.append(ele)
                k -= 1
                if k == 0:
                    return res
        
        return res
        
        