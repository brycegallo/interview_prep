// leetcode 2634 - Filter Elements from Array
// Easy - Javascript 30-Day Challenge: Day 5
//
// Given an integer array arr and a filtering function fn, return a filtered array filteredArr.
//
// The fn function takes one or two arguments:
//     arr[i] - number from the arr
//     i - index of arr[i]
//
// filteredArr should only contain the elements from the arr for which the expression fn(arr[i], i) evaluates to
// a truthy value. A truthy value is a value where Boolean(value) returns true.
// Please solve it without the built-in Array.filter method.
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const filteredArr = [];

    // for (const i in arr) {  // we use "in" here to access index
    for (let i = 0; i < arr.length; i++) {  // converting an index string to number is error prone, this is safer
        if (fn(arr[i], i)) {  // indices of arrays are strings that must be converted to numbers
            filteredArr.push(arr[i]);
        };
    };
    return filteredArr;
};
