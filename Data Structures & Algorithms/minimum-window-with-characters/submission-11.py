from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l = Counter(t)
        idx = []
        for i in range(len(s)):
            if s[i] in t:

                idx.append(i)
        
        if len(idx)==1:
            if Counter([s[idx[0]]])>= l:
                return (s[idx[0]])
            else:
                return ""
                

        i = 0
        j = 1
        minlen = float('inf')
        res = []
        substr = ""
        while(i<j and j< len(idx)):
            temp = []
            strr = s[idx[i]: idx[j]+1]
            
            for p in strr:
                if p in t:
                    temp.append(p)
                

            if Counter(temp) >= l:

                ln = len(strr)
                if ln<= minlen:
                    substr = strr
                    minlen = ln  
                i+=1
                j = max(j, i+1)
                if j>= len(idx):
                    break
                
            else:
                j+=1
            
        return (substr)