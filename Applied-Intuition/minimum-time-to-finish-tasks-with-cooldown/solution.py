from typing import List

# Minimum Time to Finish Tasks with Cooldown
# Company: Applied Intuition
# Difficulty: Medium

class Solution:
    def solve(self, n: int, tasks: List[str], k: int) -> int:
        # Keyword : Ready-Time Tracker
        # Image: A calendar marking when each task is "unlocked"
        # Workflow:
        #   1. Track each task's next available timestamp.
        #   2. Jump the clock if the task is still on cooldown.

        next_available_time = {}  # {task_name: next_earliest_start_time}
        current_time = 0

        for task in tasks:
            current_time += 1

            if task in next_available_time:
                # Key action: if still on cooldown, fast-forward the clock (Jump/Idle)
                # max ensures we never execute a task before its cooldown ends
                current_time = max(current_time, next_available_time[task])

            # Update this task's next available time (current time + cooldown k)
            next_available_time[task] = current_time + k

        return current_time


# --- Complexity Analysis ---
# Time Complexity: O(N)
#   - We iterate through the 'tasks' list exactly once.
#   - Dictionary lookups and updates are O(1) on average.
#
# Space Complexity: O(M)
#   - M is the number of unique tasks.
#   - We store one entry per unique task in the map.


# --- Test Area ---
def test():
    sol = Solution()
    n = 6
    tasks = ["A", "A", "A", "B", "B", "B"]
    k = 2
    print(f"Result: {sol.solve(n, tasks, k)}")  # Expected: 8


if __name__ == "__main__":
    test()
