class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] #result array
        candidates.sort() # sort the candidates lists
        path = [] # for finding paths 
        def backtrack(start,target):
            if target < 0:
                return 
            if target == 0:
                res.append(path[:])
                return 
            
            
            n = len(candidates)

            for i in range(start,n):
                if i > start and candidates[i] == candidates[i-1]: #skip duplicates
                    continue
                path.append(candidates[i]) #explore
                backtrack(i+1,target - candidates[i]) #reuse
                path.pop() #remove any paths

        backtrack(0,target)




        return res