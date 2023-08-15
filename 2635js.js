// leetcode 2635 - Apply Transform Over Each Element in Array
// Easy - Javascript 30-Day Challenge: Day 4
//
// Given an integer array arr and a mapping function fn, return a new array with a transformation applied to each element.
//
// The returned array should be created such that returnedArray[i] = fn(arr[i], i).
//
// Please solve it without the built-in Array.map method.
// Time: O(n) Memory: O(n)
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const result = []

    for (const i in arr) {
        result.push(fn(arr[i], Number(i)));
    }
    return result;
};