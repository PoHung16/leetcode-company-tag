# Merge Overlapping 2D Line Segment Point Sets
# Company: Applied Intuition
# Difficulty: Medium
# Link: N/A - Applied Intuition Interview Problem

from math import gcd
from collections import defaultdict
from typing import List, Tuple

# 定義型別別名
Point = Tuple[int, int]
Segment = List[Point]

def merge_2d_segments(segments: List[Segment]) -> List[Segment]:
    """
    Input Type: List[List[Tuple[int, int]]]
    Output Type: List[List[Tuple[int, int]]]

    # 思路筆記：
    # Keyword: "Merge 2D" -> 降維成 1D Interval Merge
    # Image : 想像每一條無限延伸的直線都是不同的「繩子」。
    #         我們先根據斜率和截距把珠子（線段）分到正確的繩子上，
    #         然後在每根繩子上依照座標排序，像「貪吃蛇」一樣把重疊的珠子吸在一起。

    # 3-Step Flow:
    # Step 1: Group - 透過 GCD 與截距公式，將線段分類到所屬的無限直線 (lines)。
    # Step 2: Sort & Merge - 在每條直線上，依照端點排序並執行區間合併。
    # Step 3: Result - 收集所有合併後的線段並回傳。
    """
    if not segments:
        return []

    # --- Step 1: Grouping ---
    lines = defaultdict(list)
    for seg in segments:
        p1, p2 = seg[0], seg[-1]
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]

        common = gcd(dx, dy)
        dx //= common
        dy //= common

        if dx < 0 or (dx == 0 and dy < 0):
            dx, dy = -dx, -dy

        # 唯一截距 Key，確保在同一條直線上的線段會分到同一個桶子
        intercept_key = p1[1] * dx - p1[0] * dy
        lines[(dx, dy, intercept_key)].append(seg)

    final_result = []

    # --- Step 2 & 3: Sort, Merge & Return ---
    for line_key, group in lines.items():
        # 排序珠子：Python 元組排序會先比 x，再比 y
        group.sort()

        current_seg = group[0]
        for i in range(1, len(group)):
            next_seg = group[i]

            # 貪吃蛇合併邏輯：如果當前段的尾巴 (current_seg[-1]) 碰到了下一段的頭 (next_seg[0])
            if current_seg[-1] >= next_seg[0]:
                # 伸長身體：更新尾巴到最遠處
                current_seg = [current_seg[0], max(current_seg[-1], next_seg[-1])]
            else:
                # 斷開了：存下目前的蛇，換下一條蛇開始
                final_result.append(current_seg)
                current_seg = next_seg

        final_result.append(current_seg)

    return final_result


if __name__ == "__main__":
    test_data = [
        [(1, 1), (2, 2)],
        [(2, 2), (4, 4)],
        [(10, 10), (12, 12)], # 以上三條在 y=x 上，前兩條應合併
        [(0, 0), (5, 0)],
        [(4, 0), (10, 0)]      # y=0 上的重疊線段
    ]

    res = merge_2d_segments(test_data)
    for r in res:
        print(f"Merged Segment: {r}")
