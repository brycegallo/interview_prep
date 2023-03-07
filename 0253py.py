# leetcode 0253 - Meeting Rooms II
# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of conference rooms required.
# Time O(nlogn), O(nlogn) for sorting, O(2n) for iterating through sorted start and end arrays
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([interval[0] for interval in intervals])
        ends = sorted([interval[1] for interval in intervals])
        count,result = 0, 0
        s, e = 0, 0
        while s < len(starts):
            if ends[e] > starts[s]:
                s += 1
                count += 1
                result = max(result, count)
            else:
                e += 1
                count -= 1
        return result
