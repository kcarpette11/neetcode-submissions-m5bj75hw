class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] #initialize stack
        res = 0 # initialize result
        n = len(position) # length of position


        #initialize fleet 
        fleet = [(position[i],speed[i]) for i in range(n)]
        fleet.sort(reverse=True)
        for pos, spd in fleet: # iterate through the list
            time_car = (target - pos) / spd # for calculating time

            if not stack:
                stack.append(time_car) 
            elif time_car > stack[-1]:
                stack.append(time_car) 
            
            res = len(stack)

            

        return res # return res 

        
        