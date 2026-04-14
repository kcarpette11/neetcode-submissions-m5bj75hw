class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 #  intitialize pointers
        j = len(s) - 1
        
        while i < j:
            while i < j and not s[i].isalnum(): # iterate while they do not cross
                i+= 1
            while i < j and not s[j].isalnum(): # skipping alnum char at both ends
                j -= 1
            if s[i].lower() != s[j].lower(): # if all characters mismatch
                return False
            i += 1
            j -= 1
            
        return True
            

        