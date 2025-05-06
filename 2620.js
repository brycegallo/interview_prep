// leetcode 2620 - Counter
 // Easy - Javascript 30-Day Challenge: Day 2
//
// Given an integer n, return a counter function. This counter function initially returns n
// and then returns 1 more than the previous value every subsequent time it is called (n, n + 1, n + 2, etc).
// Time: O(1) Memory: O(1)
/**
 * My Initial Solution, updated to be better
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    // let counte = -1;
    return function() {
        // counte += 1;
        // return n + counte;
        return n++;
    };
};

/**
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */