class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []


        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        print(freq)

        for i in range(k):
            max_key = max(freq, key = freq.get)
            res.append(max_key)
            del freq[max_key]
            
        return res
