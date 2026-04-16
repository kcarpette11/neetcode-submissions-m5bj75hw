import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.count = 0 # intialize count
        self.tweetMap = defaultdict(list) #initialize tweetmap
        self.followMap = defaultdict(set) #initialize followmap
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        #publish a new tweet with tweet id by userid
        #add to tweetmap
        self.tweetMap[userId].append([self.count,tweetId])
        self.count -= 1 # decrement count
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # initialize result array 
        minHeap = [] #initialize min heap

        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                for count, tweetId in self.tweetMap[followeeId]:
                    heapq.heappush(minHeap,[count,tweetId])
        
        while minHeap:
            count, tweetId = heapq.heappop(minHeap)
            res.append(tweetId)

            if len(res) == 10:
                break
        return res
     

    
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId: # to make sure that the user with followerId follows the followeeId
            self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #to unfollower the user with followeeId
        self.followMap[followerId].discard(followeeId)
        
