Five-Minute Demo Script

Introduction (30 seconds): Explain that the goal is to find the minimum number of rooms needed for overlapping meetings.

Input (45 seconds): Open meetings.csv and explain the Meeting, Start, and End columns.

Algorithm (90 seconds): Explain sorting by start time and using a min-heap to track the earliest room availability.

Run (60 seconds): Run python main.py and show the minimum room count and generated benchmark file.

Tests and complexity (45 seconds): Run python -m unittest -v. State the time complexity O(n log n) and space complexity O(n).

Reflection (30 seconds): Mention that the heap avoids checking every room for each meeting, and suggest adding a room-by-room visual schedule.