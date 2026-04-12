# Minimum Time to Finish Tasks with Cooldown

**Company:** Applied Intuition
**Difficulty:** Medium

## Problem

You are given a sequence of tasks `tasks` (array of strings) that must be executed in the given order. Between two executions of the same task, there must be at least `k` time units of cooldown.

At each time unit, you can either:
- Execute the next task in the sequence (if it does not violate cooldown), or
- Stay idle for 1 time unit.

Return the minimum total time to finish all tasks.

## Examples

**Example 1:**

Input:
```
6
A A A B B B
2
```

Output:
```
8
```

One optimal schedule is `A B idle A B idle A B`.

## Constraints

- `1 <= n <= 2e5`
- `0 <= k <= 2e5`
- Task name length `<= 10`
