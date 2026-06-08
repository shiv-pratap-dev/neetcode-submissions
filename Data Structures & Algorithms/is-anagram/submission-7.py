class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # freq ={}
        # freq_2 = {}
        # for ch in s:
        #     if ch in freq:
        #         freq[ch] +=1
        #     else:
        #         freq[ch] = 1
        
        # for ch in t:
        #     if ch in freq_2:
        #         freq_2[ch] +=1
        #     else:
        #         freq_2[ch] = 1
            
        
        # return freq == freq_2

        sortedS = sorted(s)
        sortedT = sorted(t)
        
        return sortedS == sortedT


        