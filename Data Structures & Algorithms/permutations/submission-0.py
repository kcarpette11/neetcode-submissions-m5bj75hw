class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums) #length of nums 
        used = set() #used for lookups
        if n == 0:
            return [[]]
        def backtrack():
            if len(path) == n:
                res.append(path[:])
                return
            

            for num in nums:
                if num not in used:
                    used.add(num)
                    path.append(num)
                    backtrack()
                    path.pop()
                    used.remove(num)


        backtrack()




        return res