// leetcode 2665 - Counter II
 // Easy - Javascript 30-Day Challenge: Day 3
//
// Write a function createCounter. It should accept an initial integer init. It should return an object with three functions.
//
// The three functions are:
//
//     increment() increases the current value by 1 and then returns it.
//     decrement() reduces the current value by 1 and then returns it.
//     reset() sets the current value to init and then returns it.
// Time: O(1) Memory: O(1)
/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let count = init;

    const increment = () => ++count;
    const decrement = () => --count;

    function reset() {
        count = init;
        return count;
    }

    return {
        increment,
        decrement,
        reset,
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */