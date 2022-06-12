class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        result = []
        start = intervals[0][0]
        end = intervals[0][1]
        n = len(intervals)
        for i in range(1, n):
            current = intervals[i]
            if  intervals[i][0] >= start and  intervals[i][1] <= end:
                continue
            elif  intervals[i][0] > end:
                result.append([start, end])
                start =  intervals[i][0]
                end =  intervals[i][1]
            elif  intervals[i][0] >= start and  intervals[i][1] >= end:
                end =  intervals[i][1]

        result.append([start, end])
        return result