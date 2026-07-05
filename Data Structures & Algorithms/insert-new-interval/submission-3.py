class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        """

        convert intervals into events. start adds 1, end removes 1
        we get a line of 0s and non 0 events down a line.

        now, how do we scan our line our line?

        if our current thickness = 0 and we encounter a start event, ready to add a new interval
        if we encounter an end event and our thickness drops to zero, ready to close the interval and add int
        
        1, create events



        """

        intervals.append(newInterval)

        events = []

        for a, b in intervals:

            events.append((a, 1))
            events.append((b, -1))

        events.sort(key=lambda x: (x[0], -x[1]))
    
        output = []

        current_width = 0
        current_start = 0
        current_end = 0

        print(events)

        for ts, e in events:

            current_width += e

            if current_width == 1:
                if e == 1:
                    current_start = ts

            elif current_width == 0:
                current_end = ts
                output.append([current_start, current_end])

        return output
        