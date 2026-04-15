# Merge Overlapping 2D Line Segment Point Sets
# Company: Applied Intuition
# Difficulty: Medium
# Link: N/A - Applied Intuition Interview Problem

# keyword: Merge Interval -> simplify it into a 1D Interval Merge
# Image: : Imagine every infinite line in 2D space is a different "string". We group them by slope, sort them, and merge them
# Workflow:
    # Step 1: Grouping –  Categorize segments 
        # Slope - normalize with GCD + normalize with direction to have same slope
        # Intercept
    # Step 2: Sort & Merge – On each line, sort & merge to perform a standard interval merge.
    # Step 3: Result – Collect the final merged segments and return the list.
# Tricks
    # if hashmap's key contains multiple value: use defaultdict(list) 
    # If you want to traverse a map, map.items() or map.keys() or map.values()
    # Hashmap key cannot be list


from math import gcd
from collections import defaultdict
from typing import List, Tuple

Point = Tuple[int, int]
Segment = List[Point]

def merge_2d_segments(segments: List[Segment]) -> List[Segment]:
    """
    Input: A list of line segments (each defined by a start and end point).
    Output: A list of merged segments where overlaps are removed.
    """
    if not segments:
        return []

    # --- Step 1: Grouping ---
    # We use a dictionary to group segments that lie on the exact same infinite line.
    lines = defaultdict(list)
    for seg in segments:
        p1, p2 = seg[0], seg[-1]
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]

        # Normalize the direction vector using GCD
        common = gcd(dx, dy)
        dx //= common
        dy //= common

        # Ensure a consistent direction (vector "canonical form")
        if dx < 0 or (dx == 0 and dy < 0):
            dx, dy = -dx, -dy

        # Calculate a unique intercept key to distinguish parallel lines.
        # Derived from the line equation: dy*x - dx*y = constant
        intercept_key = p1[1] * dx - p1[0] * dy
        lines[(dx, dy, intercept_key)].append(seg)

    final_result = []

    # --- Step 2 & 3: Sort, Merge & Return ---
    for line_key, group in lines.items():
        # Sorting the "beads": Python sorts tuples by x-coord first, then y-coord.
        group.sort()

        current_seg = group[0]
        for i in range(1, len(group)):
            next_seg = group[i]

            # "Snake" merge logic: 
            # If the tail of our current segment reaches the head of the next one...
            if current_seg[-1] >= next_seg[0]:
                # Stretch the tail to the furthest point reachable.
                current_seg = [current_seg[0], max(current_seg[-1], next_seg[-1])]
            else:
                # There's a gap! Save the current segment and start a new "snake."
                final_result.append(current_seg)
                current_seg = next_seg

        # Don't forget to add the last segment of the group
        final_result.append(current_seg)

    return final_result

# ==========================================
# Complexity Analysis:
#
# Time Complexity: O(n log n)
# - Grouping: O(n), we touch each segment once.
# - Sorting: O(n log n), this is the bottleneck as we sort all segments.
# - Merging: O(n), we process each segment in the sorted groups once.
#
# Space Complexity: O(n)
# - We create size N list(add up all keys: segments) and size N final_result
# ==========================================
if __name__ == "__main__":
    test_data = [
        [(1, 1), (2, 2)],
        [(2, 2), (4, 4)],
        [(10, 10), (12, 12)], # 以上三條在 y=x 上，前兩條應合併
        [(0, 0), (5, 0)],
        [(4, 0), (10, 0)]      # y=0 上的重疊線段
    ]

    res = merge_2d_segments(test_data)
    print(f"merge_2d_segments: {res}")
