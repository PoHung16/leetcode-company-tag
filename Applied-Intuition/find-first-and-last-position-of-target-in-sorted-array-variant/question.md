# Find the First and Last Position of a Target in a Sorted Array (Variant)

**Company:** Applied Intuition
**Difficulty:** Medium

## Problem

Given a non-decreasing sorted integer array `nums` of length `n` and an integer `target`, return the starting index and ending index (0-based) of `target` in the array.

If `target` does not exist in the array, return `-1 -1`.

**Requirement:** Design an algorithm with O(log n) time complexity.

## Input / Output

**Input (stdin)**
- Line 1: integer `n`
- Line 2: `n` integers representing `nums`
- Line 3: integer `target`

**Output (stdout)**
- Print two integers: `start end`

## Examples

**Input:**
```
n = 6
nums = [5, 7, 7, 8, 8, 10]
target = 8
```

**Output:**
```
3 4
```

## Constraints

- `0 <= n <= 2 * 10^5`
- `-10^9 <= nums[i], target <= 10^9`
- `nums` is sorted in non-decreasing order
