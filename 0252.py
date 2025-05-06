# leetcode 0252 - Meeting Rooms
# Given an array of meeting time intervals where intervals[i] = [starti, endi],
# determine if a person could attend all meetings.
# Time O(nlogn), O(nlogn) for sorting, O(n) for iterating through sorted intervals array
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort( key = lambda i : i[1])
        print(intervals)

        for i in range(1, len(intervals)):
            interval1 = intervals[i - 1][1]
            interval2 = intervals[i][0]
            if interval1 > interval2:
                return False
        return True
