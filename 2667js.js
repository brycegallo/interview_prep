 // leetcode 2667 - Create Hello World Function
 // Easy - Javascript 30-Day Challenge
 // Write a function createHelloWorld. It should return a new function that always returns "Hello World".
 // Time: O(1) Memory: O(1)
 /**
 * @return {Function}
 */
var createHelloWorld = function() {
    return function(...args) {
        return "Hello World";
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */
