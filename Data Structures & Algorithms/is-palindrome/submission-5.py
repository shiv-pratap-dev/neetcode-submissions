class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = ""

        for i in s:
            if (i.isalnum()):
                rev += i.lower()
        
        if rev == rev[::-1]:
            return True
        else:
            return False
        