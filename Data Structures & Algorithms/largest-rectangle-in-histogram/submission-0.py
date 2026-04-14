class Solution:
        def largestRectangleArea(self, heights: List[int]) -> int:
            stack = []  # initialize stack to store indices
            n = len(heights)
            max_area = 0
            
            for i in range(n + 1):  # iterate through array + sentinel
                # Get current height (0 for sentinel at the end)
                current_height = heights[i] if i < n else 0
                
                # While stack is not empty and current height is less than the height at top of stack
                while stack and current_height < heights[stack[-1]]:
                    # Pop the top element from stack and get its height
                    height_index = stack.pop()
                    height = heights[height_index]
                    
                    # Calculate width: if stack is empty, width is i, else i - stack[-1] - 1
                    width = i if not stack else i - stack[-1] - 1
                    
                    # Update max area - use height * width, not height_index * width
                    max_area = max(max_area, height * width)
                
                stack.append(i)  # push current index into stack
            
            return max_area