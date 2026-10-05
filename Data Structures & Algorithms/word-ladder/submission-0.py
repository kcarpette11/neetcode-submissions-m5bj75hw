from collections import deque
from typing import List 
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 
        
        res = 1

        m,n = len(wordList),len(wordList[0])
        visited = set()
        queue = deque([beginWord])
        visited.add(beginWord)
        words = set(wordList)

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return res

                for neighbor in words:
                    if neighbor in visited:
                        continue
                    
                    differences = sum(a != b for a, b in zip(word,neighbor))

                    if differences == 1:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
           

            res += 1 


        return 0
        