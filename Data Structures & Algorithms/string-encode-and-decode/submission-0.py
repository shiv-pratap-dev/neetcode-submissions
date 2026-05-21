class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            l = str(len(i))
            s += l+'#'+i
            
        return s

    

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        start = 0

        while(i < len(s)):
            if s[i] == '#':
                l= int(s[start:i])
                res.append(s[i+1 : i+1+l])
                
                i = i+l+1
                start = i
            else:
                i+=1
            
        return res
