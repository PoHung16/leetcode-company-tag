# Merge Overlapping 2D Line Segment Point Sets

**Company:** Applied Intuition
**Difficulty:** Medium

## Problem

You are given `segments`, a list of 2D lists. Each element is a sequence of discrete points on a line segment, where each point is represented as `(x, y)`.

You may assume: within each segment, points are already sorted along the segment order.
You may NOT assume: any ordering among different segments.

Two segments can be merged if:
- They are collinear (lie on the same infinite line), and
- Their point sets overlap (they share at least one identical point).

The merged segment is the union of their points, de-duplicated and sorted along the segment order.

Return the list of all segments after repeatedly merging all mergeable segments.

## Examples

**Input:**
```
[[(1, 1), (2, 2), (4, 4)],
 [(2, 1), (4, 2)],
 [(3, 3), (6, 6)],
 [(7, 7), (8, 8)]]
```

**Output:**
```
[[(1, 1), (2, 2), (3, 3), (4, 4), (6, 6)],
 [(7, 7), (8, 8)],
 [(2, 1), (4, 2)]]
```

## Constraints

- Coordinates are integers.
- Each segment contains at least 2 points.
- Output segment order does not matter, but points within each returned segment must be in-order and unique.
