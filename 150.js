// leetcode 0150 - Evaluate Reverse Polish Notation
// You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
//
// Evaluate the expression. Return an integer that represents the value of the expression.
//
// Note that:
//     The valid operators are '+', '-', '*', and '/'.
//     Each operand may be an integer or another expression.
//     The division between two integers always truncates toward zero.
//     There will not be any division by zero.
//     The input represents a valid arithmetic expression in a reverse polish notation.
//     The answer and all the intermediate calculations can be represented in a 32-bit integer.
/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    let stack = [];

    for (const t of tokens) {
        if (t === '+') { stack.push(stack.pop() + stack.pop()) }
        else if (t === '*') { stack.push(stack.pop() * stack.pop()) }
        else if (t === '-') {
            let a = stack.pop(), b = stack.pop()
            stack.push(b - a)
        }
        else if (t === '/') {
            let a = stack.pop(), b = stack.pop()
            stack.push(parseInt(b / a))
        }
        else stack.push(parseInt(t));
    }
    return stack[0];
};