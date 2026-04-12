# Stream Simulation — Detect Short vs. Long Press from Button State Changes

**Company:** Applied Intuition
**Difficulty:** Medium

## Problem

You are given a real-world streaming input representing the state of a button (or buttons) over time:

- `1` means the button is pressed (on)
- `0` means the button is released (off)

Write a program/function to process this stream and detect complete press cycles (`0 -> 1 -> 0`). For each completed press, output whether it is a **short press** or a **long press** based on how long the button stayed pressed.

## Requirements

- Use system time to obtain the current time (e.g., `System.currentTimeMillis()` in Java) and compute press duration.
- When the state transitions from `1` to `0` (release), classify the press as short/long and output the result.
- Passing the provided test cases is sufficient.

## Details Typically Clarified During Interview

- The structure of each stream event (just state? or includes buttonId/timestamp?)
- The long-press threshold (e.g., 500ms / 1000ms)
- Output format and when to output (on press vs. on release)

## Examples

**Input state stream:** `0, 1, 1, 1, 0`

- If press duration > threshold: output `LONG_PRESS`
- Else output `SHORT_PRESS`

**Example:**

Input (concept): states `0 1 0` with press duration 200ms, threshold 800ms

Output:
```
SHORT_PRESS
```

## Constraints

- Stream events arrive in order.
- Each event contains a button ID and its current state (0 or 1).
- The long-press threshold is configurable (default: 500ms).
- Multiple buttons may be tracked independently.
