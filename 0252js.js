// leetcode 0252 - Meeting Rooms
// Given an array of meeting time intervals where intervals[i] = [starti, endi],
// determine if a person could attend all meetings.
// Time O(nlogn), O(nlogn) for sorting, O(n) for iterating through sorted intervals array
/**
 * @param {number[][]} intervals
 * @return {boolean}
 */
var canAttendMeetings = function(intervals) {
    intervals = intervals.sort((a, b) => a[0] - b[0]); // sort by first column in 2d array
    console.log(intervals)
    for (let i = 1; i < intervals.length; i++) {
        let interval1 = intervals[i-1]
        let interval2 = intervals[i]
        if (interval1[1] > interval2[0]) {
            return false
        }
    }
    return true
};