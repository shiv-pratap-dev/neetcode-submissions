class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        seq = []

        for i in range(len(s)):
            if s[i] not in seq:
                seq.append(s[i])
            
            else:
                j = seq.index(s[i])
                seq = seq[j+1:]
                seq.append(s[i])
            
            max_len = max(max_len , len(seq))

        return(max_len)