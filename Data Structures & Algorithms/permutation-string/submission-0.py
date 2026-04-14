class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): # checking length of 2 strings match
            return False
       

        #count frequency of both strings, window size is 26
        # as in 26 letters in the alphabet 
        s1_count, s2_count = [0] * 26, [0] * 26

        #update frequencies and counts, initialize the window
        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord('a')] += 1
            s2_count[ord(s2[i])-ord('a')] += 1
            # slide over the window to s2
        for i in range (len(s2)-len(s1)):
            if s1_count == s2_count:
                return True
            s2_count[ord(s2[i])-ord('a')] -= 1
            s2_count[ord(s2[i+len(s1)])- ord('a')] += 1

        #check the last window
        return s1_count == s2_count 

       


        
        
        