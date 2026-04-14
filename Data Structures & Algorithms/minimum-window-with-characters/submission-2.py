class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): # if the length of s is less than length of t
            return ""
        i = 0
       
        min_length = float('inf')
        i_index = -1 # no window found

        s_count = [0] * 256 # tracking counts of 2 arrays when it comes to chars
        t_count = [0] * 256
        #count occurances in t
        for char in t:
            t_count[ord(char)] += 1 # ord returns the unicode code for char 
        count = 0

      


        for j in range(len(s)):
            # count occurances in s 
            s_count[ord(s[j])] += 1

            # if the chars match for both strings, update count
            if t_count[ord(s[j])] != 0 and s_count[ord(s[j])] <= t_count[ord(s[j])]:
                count += 1
            
            if count == len(t): # if all characters match
                while s_count[ord(s[i])] > t_count[ord(s[i])] or t_count[ord(s[i])] == 0:
                    if s_count[ord(s[i])] > t_count[ord(s[i])]:
                        s_count[ord(s[i])] -= 1
                    i += 1 # minimize window
                length = j - i + 1 # update window size

                if min_length > length:
                    min_length = length
                    i_index = i
                
        if i_index == -1:
            return ""
          

        return s[i_index:i_index + min_length]


                    
                    
            




        
        