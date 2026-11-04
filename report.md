Meeting Rooms — Project Report

1. Problem

The Meeting Rooms problem asks for the minimum number of meeting rooms needed to host a set of meetings without assigning overlapping meetings to the same room. Each meeting has a start time and an end time.

2. Method

The solution uses a Greedy strategy supported by a Min-Heap:

Sort all meetings by their start times.

Store the end times of meetings currently occupying rooms in a min-heap.

For each meeting, compare its start time with the earliest end time in the heap.

If the earliest meeting has ended (end <= start), reuse that room by removing its end time.

Insert the current meeting's end time.

The largest heap size represents the minimum number of rooms required.

3. Complexity Analysis

Sorting the meetings requires O(n log n). Every meeting is pushed into the heap once and can be popped at most once. Heap operations therefore take O(n log n) in total. The overall time complexity is O(n log n) and the auxiliary space complexity is O(n).

4. Experiments

The program runs five trials for each input size (100, 500, 1,000, 2,000, 4,000, and 8,000 meetings) and records the average execution time in benchmark_results.csv. Runtime depends on the computer and Python environment. The experiment is intended to show how execution time grows as the number of meetings increases.

5. Conclusion

A Min-Heap efficiently tracks the room that becomes available first. Combined with sorting, it provides an O(n log n) solution and correctly handles meetings that start exactly when another meeting ends.

Reflection

What surprised you? A single min-heap is enough to track room availability without checking every room for every meeting.

What would you do next? Add a visual schedule showing which meeting is assigned to each room and compare the heap solution with a simpler approach.