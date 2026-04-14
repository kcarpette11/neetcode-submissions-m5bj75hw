class Solution:
    def isValid(self, s: str) -> bool:
       
        stack = [] # initialize list for stack
        char_mapping = {'(':')','{':'}','[':']'}

        #adding elements into stack
        for ch in s:
            if ch in char_mapping:
                stack.append(char_mapping[ch]) # push expected closingg bracket
            elif stack and stack[-1] == ch:
                stack.pop() # remove last element(FILO)
            else:
                return False
        return (len(stack) == 0) # if stack is empty 


            
            

        

        