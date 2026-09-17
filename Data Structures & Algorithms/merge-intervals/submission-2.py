class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by their start time so we can process
        # potentially overlapping intervals in order
        intervals.sort(key=lambda pair:pair[0])

        # Initialize the output with the first interval
        output = [intervals[0]]

        # Compare each interval with the last one,
        for start, end in intervals:
            last_end = output[-1][1]

            # If the current interval overlaps with the last one,
            # extend the end boundary if necessary
            if start <= last_end:
                output[-1][1] = max(last_end, end)
            
            else:
                output.append([start, end])
        
        return output
