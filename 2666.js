// leetcode 2666 - Allow One Function Call
// Easy - Javascript 30-Day Challenge: Day 8
//
// Given a function fn, return a new function that is identical to the original function except that it ensures fn is called at most once.
//
//     The first time the returned function is called, it should return the same result as fn.
//     Every subsequent time it is called, it should return undefined.
/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    var called = true;
    return function(...args){
        if (called == true) {
            called = false;
            return fn(...args);
        }

    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */