
class Solution:
 def leastInterval(self, tasks: List[str], n: int) -> int:
    t = len(tasks)  # length of array
    
    count = [0] * 26  # frequency array
    
    for task in tasks:
        count[ord(task) - ord('A')] += 1  # uppercase fix
    
    max_freq = max(count)
    max_count = count.count(max_freq)
    
    return max(t, (max_freq - 1) * (n + 1) + max_count)
        

         
              
   
  




        