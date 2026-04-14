class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #initialize stack
       
        n = len(temperatures) # length of array
        result = [0] * n # for output


        for i in range(n - 1, -1, -1):  # doing reverse approach
            while stack and temperatures[stack[-1]] <= temperatures[i] :
                stack.pop() # pop indoces where the values are smaller than the current element 
            if stack:
                result[i] = stack[-1] - i
            else:
                result[i] = 0
            
           
            stack.append(i)
            
       


        return result

    
        
        