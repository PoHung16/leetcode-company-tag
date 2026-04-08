# Find the First and Last Position of a Target in a Sorted Array (Variant)
# Company: Applied Intuition
# Difficulty: Medium
# Link: N/A - Applied Intuition Interview Problem

from typing import List, Tuple

# Keyword: "Sorted array, Find Answer's Range" -> Binary Search
# Image: "The Wall Seeker" - 找到目標後不要停，繼續往左/右摸直到撞到邊界的牆。
# 3-Step Flow:
#    Step 1: Initialize left, right pointer (and a 'bound' to record the index).
#    Step 2: Traverse with l, r (When matched, update bound and move towards the wall).
#    Step 3: Result (Run twice to get start and end).

def find_range(nums: List[int], target: int) -> Tuple[int, int]:
    """
    Input Type: List[int], int
    Output Type: Tuple[int, int]
    """

    # 定義輔助函式，用 bias 決定我們要找左牆還是右牆
    def search(find_left_bias: bool) -> int:
        # Step 1: Initialize
        l, r = 0, len(nums) - 1
        bound = -1

        # Step 2: Traverse (Binary Search Logic)
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                # 關鍵點：記錄當前位置 (Record)
                bound = mid
                if find_left_bias:
                    # 繼續往左縮小範圍，試圖撞到左邊界 (Push left boundary)
                    r = mid - 1
                else:
                    # 繼續往右縮小範圍，試圖撞到右邊界 (Push right boundary)
                    l = mid + 1
        return bound

    # Step 3: Result
    # 第一次執行：鎖定左邊界
    start = search(find_left_bias=True)

    # Edge Case: 如果找不到起點，代表 target 不存在，直接回傳 -1, -1
    if start == -1:
        return (-1, -1)

    # 第二次執行：鎖定右邊界
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
