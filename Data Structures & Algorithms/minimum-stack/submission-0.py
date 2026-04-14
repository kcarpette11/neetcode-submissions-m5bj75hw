class MinStack:

    def __init__(self):
        self.stack = []  #initialize stack
        

    def push(self, val: int) -> None:
        self.stack.append(val) # pushing val into stack
        

    def pop(self) -> None:
        self.stack.pop() # removing element in stack
        

    def top(self) -> int:
        return self.stack[-1] # for finding the top element of the stack

        

    def getMin(self) -> int: # finding minimum element of stack 
        return min(self.stack)
        
