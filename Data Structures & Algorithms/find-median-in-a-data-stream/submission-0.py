import heapq # for heap

class MedianFinder:

    def __init__(self):
        #initialize object 

        self.small = [] #for max heap, storing smaller half 
        self.large = [] # for min  heap, storing larger half
        

    def addNum(self, num: int) -> None:
        #adding num to data stream
        self.num = num 
        if self.large and self.num > self.large[0]:
            #if  min heap and integer is greater than the first element in heap, add to heap
            heapq.heappush(self.large,self.num) 
        
        else:
            # add to max heap 
            heapq.heappush(self.small,-self.num)
        
        #rebalance sizes
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small,-heapq.heappop(self.large))
        
        #in case if there is any ordering to be done
        if self.small and self.large and (-self.small[0] >self.large[0]):
            small_top = -heapq.heappop(self.small)
            large_top = heapq.heappop(self.large)
            heapq.heappush(self.small,-large_top)
            heapq.heappush(self.large,small_top)
    
        

    def findMedian(self) -> float:
        #find the median of all the elements
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0
        
        