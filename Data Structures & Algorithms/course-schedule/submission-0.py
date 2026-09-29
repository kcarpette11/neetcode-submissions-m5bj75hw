class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites :
            return True

        path, done = set(), set() # for tracking the nodes

        graph =[[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)

       

        def dfs(course):
            if course in path:
                return False
            
            if course in done:
                return True 
            path.add(course)

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False 

            path.remove(course)
            done.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        
        