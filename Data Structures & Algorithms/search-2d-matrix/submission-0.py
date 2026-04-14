class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #using binary search to search through matrix 
        m = len(matrix) # m is the number of rows 
        n = len(matrix[0]) # n is the number of columns

        #initialize the pointers

        left, right = 0, m * n - 1

        while left <= right :
            mid = left + (right - left) // 2 #for finding the middle element
            row = mid // n
            col = mid % n 
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            elif matrix[row][col] > target:
                right = mid - 1 
        return False
          

        