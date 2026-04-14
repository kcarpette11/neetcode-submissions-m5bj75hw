class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] # initialize stack 
        result = 0 # initialize result
        # iterate through the array to check for operators and operands
        for token in tokens: 
            # Encounter operator, remove two elements from stack
            if token in {"+","-","*","/"}: # to check if any of the tokens are these operations
                b = stack.pop()
                a = stack.pop()

          
            if token == "+": 
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))
            else:
                stack.append(int(token)) # add integer into stack
            result = stack[0] # result is the first element in stack as integer
        return result
        
            
           



        