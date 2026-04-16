# Minimum Time to Finish Tasks with Cooldown
# Company: Applied Intuition
# Difficulty: Medium

# Keyword : minimum number  -> Greedy with sort/ hashmap
    # Greedy is basically making the local optimal solution and hoping it leads to the global optimal solution
# Image: A hashmap tracking each task "next_available time". you check if a Key or Value exists before , then perform following actions
# Workflow - 3 Step:
    #  Step 1: Initialize Current Time & hashmap Tracker
    #  Step 2: Traverse the array to check if a  a Key or Value exists before, then perform following actions
    #  Step 3: Return result
from typing import List
def solve(n: int, tasks:List[str], k: int) -> int:
    next_available_time = {} # {taskName : next_available_time}
    current_time = 0
    for i in range(len(tasks)):
        current_time += 1
        if tasks[i] in next_available_time:
            current_time = max(current_time,next_available_time[tasks[i]])
        next_available_time[tasks[i]] = current_time+k+1
    return current_time
    
# --- Complexity Analysis ---
# Time Complexity: O(N)
#   - Traverse size N Array
#
# Space Complexity: O(M)
#   - we create size M Map
#   - M is the number of unique tasks.

def test():
    #sol = Solution()
    #sol.find_range(6,nums_example,target_example)
    n = 6
    tasks = ["A", "B", "A", "B", "A", "B"]
    k = 2
    result = solve(n,tasks,k)
    print(f"Result:{result}")
    
if __name__ == "__main__":
    test()
    
    



