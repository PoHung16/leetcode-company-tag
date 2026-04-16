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
class Solution:
    def solve(self, n: int, tasks: List[str], k: int) -> int:
        next_avaliable_time = {} # {task_name: next_earliest_start_time}
        current_time = 0
        for task in tasks:
            current_time += 1
            if task in next_avaliable_time:
                current_time = max(current_time, next_available_time[task])
            # Update this task's next available time (current time + cooldown k)
            next_available_time[task] = current_time + k
        return current_time


# --- Complexity Analysis ---
# Time Complexity: O(N)
#   - Traverse size N Array
#
# Space Complexity: O(M)
#   - we create size M Map
#   - M is the number of unique tasks.


# --- Test Area ---
def test():
    sol = Solution()
    n = 6
    tasks = ["A", "A", "A", "B", "B", "B"]
    k = 2
    print(f"Result: {sol.solve(n, tasks, k)}")  # Expected: 8
if __name__ == "__main__":
    test()
