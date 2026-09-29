class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

            path, done = set(), set() # for tracking the nodes
            order = [] # for adding courses 

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
                order.append(course) # added after prerequisites
                return True
            
            for course in range(numCourses):
                if not dfs(course):
                    return []
            return order
            
       
        

        