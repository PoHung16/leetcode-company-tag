# Find the First and Last Position of a Target in a Sorted Array (Variant)
# Company: Applied Intuition
# Difficulty: Medium
# Link: N/A - Applied Intuition Interview Problem

from typing import List, Tuple

# Keyword: "Sorted Array -> Basic Binary Search
# Image: "Check the mid value, if target < mid , search on left side, if target > mid , search on right side
# Workflow - 3 Steps:
#    Step 1: Initialize left, right pointer (and a 'bound' to record the index).
#    Step 2: Traverse the array with l,r pointer (Perform Binary Search)
#    Step 3: Result 

def find_range(nums: List[int], target: int) -> Tuple[int, int]:
    """
    Input Type: List[int], int
    Output Type: Tuple[int, int]
    """

    # 定義輔助函式，用 bias 決定我們要找左牆還是右牆
    def search(find_left_bias: bool) -> int:
        l, r = 0, len(nums) - 1
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                # 關鍵點：記錄當前位置 (Record)
                ans = mid
                if find_left_bias:
                    # Push left boundary
                    r = mid - 1
                else:
                    # Push right boundary
                    l = mid + 1
        return ans

    # First Time: Seacrh for left side bound
    start = search(find_left_bias=True)

    # if you can not find the start, return -1, -1
    if start == -1:
        return (-1, -1)

    # Second Time: Seacrh for right side bound
    end = search(find_left_bias=False)

    return (start, end)

# ==========================================
# Complexity Analysis:
# Time Complexity: O(log n)
# - 我們執行了兩次獨立的 Binary Search，每次都是 O(log n)。
# - 2 * O(log n) 在 Big O 表示法中簡化為 O(log n)。
#
# Space Complexity: O(1)
# - 只使用了常數個變數 (l, r, mid, bound)，
# - 不隨輸入陣列的大小 n 而增加額外空間負擔。
# ==========================================



if __name__ == "__main__":
    nums_example = [5, 7, 7, 8, 8, 10]
    target_example = 8

    print(f"Input: {nums_example}, target: {target_example}")
    start_idx, end_idx = find_range(nums_example, target_example)
    print(f"Output: {start_idx} {end_idx}")
