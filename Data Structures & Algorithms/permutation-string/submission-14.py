class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        isPerm = False
        
        for i in range(len(s2) - len(s1) +1):
            if sorted(list(s2[i: i+len(s1)])) == sorted(list(s1)):
                isPerm = True
                break
            else:
                isPerm = False
                
     
        return (isPerm)  
        