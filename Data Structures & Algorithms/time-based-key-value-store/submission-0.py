class TimeMap:

    def __init__(self):
        self.store = {} # intialize dictionary  for list of vals with timestamp
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [] # store into set
        self.store[key].append([value, timestamp]) #add into dict


        

    def get(self, key: str, timestamp: int) -> str:
        #using binary search
        res, vals = "", self.store.get(key,[]) # initialite keys and values for out put
        n = len(vals) # length of array
        l, r = 0, n - 1 # initialize pointers

        while l <= r:
            mid = (l + r) // 2 # calculate middle element/index
            if vals[mid][1] <= timestamp:
                res = vals[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res

        
        
