class Solution:
    def isPalindrome(self,s): # to check for valid palindromes 
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

    def partition(self, s: str) -> List[List[str]]:
        s_count = len(s) # length of string 
        res = [] 
        path = []
        def backtrack(i):
            if i >= s_count:
                res.append(path.copy()) # add copy of path to result
                return
            for j in range(i, s_count):
                substring = s[i:j+1]
                if self.isPalindrome(substring):
                    path.append(substring)
                    backtrack(j + 1)
                    path.pop()

        backtrack(0)
        return res