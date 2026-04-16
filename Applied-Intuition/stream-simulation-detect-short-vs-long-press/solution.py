# Stream Simulation — > OOD: need memory
# Company: Applied Intuition
# Difficulty: Medium

"""
# A. Clarify the goal:
#    - Process a stream of button states (0/1) to detect full press cycles (0 -> 1 -> 0).
#    - Record the exact timestamp of the "Press" event (0 -> 1).
#    - Calculate duration on release (1 -> 0) to classify as SHORT_PRESS or LONG_PRESS.

# B. Decide the Data Structure:
#    - press_starts (Map): {button_id: timestamp} tracks start time of current press.
#    - last_states (Map): {button_id: state} tracks previous signal to detect signal switch
#    - threshold: Cutoff time in milliseconds (e.g., 500ms).

# C. Implement constructor & method:
#    - Detect "Rising Edge" (0 -> 1) to start timer.
#    - Detect "Falling Edge" (1 -> 0) to end timer, pop data, and classify.
#    - Always update last_state at the end of every event.
"""

import time
class ButtonDetector:
    def __init__(self, threshold_ms=500):
        self.threshold = threshold_ms
        self.press_starts = {} #{button_id: timestamp}
        self.last_states = {} #{button_id: state}

    def process_event(self, button_id, current_state):
        current_time = int(time.time() * 1000) # make it millsecond
        prev_state = self.last_states.get(button_id,0)
        # Case 1: 0 -> 1 (Rising Edge)
        if prev_state == 0 and current_state == 1:
            self.press_starts[button_id] = current_time
        # Case 2: 1 -> 0 (Falling Edge)
        elif prev_state == 1 and current_state == 0:
            if button_id in self.press_starts:
                start_time = self.press_starts[button_id]
                duration = current_time - start_time
                if duration >= self.threshold:
                    self._output(button_id, "LONG_PRESS", duration)
                else:
                    self._output(button_id, "SHORT_PRESS", duration)               

        # Keep the "Memory" alive by updating last_state
        self.last_states[button_id] = current_state

    def _output(self, bid, result, duration):
        print(f"[Result] Button {bid}: {result} ({duration}ms)")


# --- Test Case ---
def test():
    detector = ButtonDetector(threshold_ms=500)
    print("--- Start Stream Simulation ---")

    # Short Press Test
    detector.process_event("A", 1)
    time.sleep(0.2)
    detector.process_event("A", 0)

    # Long Press Test
    detector.process_event("B", 1)
    time.sleep(0.7)
    detector.process_event("B", 0)


if __name__ == "__main__":
    test()

# --- Complexity Analysis ---
# Time Complexity: O(1) per event.
#   - Accessing and updating the hash map takes constant time.
# Space Complexity: O(B).
#   - B is the number of buttons being tracked. We store two entries per button.
