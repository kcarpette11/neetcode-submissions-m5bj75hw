# use quick select to find kth largest element in array
from typing import List
class Solution:
    def partition(self,arr, left, right):
        x = arr[right]
        i = left
        for j in range(left,right):
            if arr[j] <= x:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[right] = arr[right], arr[i]
        return i 
    def quickselect(self,arr,left,right,k):
        if left == right:
            return arr[left]
        pivot_index = self.partition(arr,left,right)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            return self.quickselect(arr,pivot_index + 1,right,k)
        else:
            return self.quickselect(arr,left,pivot_index - 1,k)
    def findKthLargest(self, nums: List[int], k: int) -> int: 
        if k <= 0 or k > len(nums): # to look for kth largest
            return -1
        #convert to kth smallest
        k = len(nums) - k
        return self.quickselect(nums,0,len(nums) - 1,k)
     

       


        