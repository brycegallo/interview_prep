// leetcode 0053 - Maximum subarray
// Given an integer array nums, find the subarray with the largest sum, and return its sum.
//
// notes
// could do for i=0 in nums, for j=i in nums, for k=i in nums and compute value of every subarray
// but this would be incredibly wasteful
//
// sliding window solution
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let maxSub = nums[0], cSum = 0;

    for (const n of nums) {
        cSum *= cSum > 0;
        cSum += n;
        maxSub = Math.max(cSum, maxSub)
    }
    return maxSub;
};