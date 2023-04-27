// leetcode 0371 - Sum of Two Integers
// Given two integers a and b, return the sum of the two integers
// without using the operators + and -.
// Time: O(1) Memory: O(1)

// old solution
// class Solution {
//     public int getSum(int a, int b) {
//         while (b != 0) {
//             int tmp = (a & b) << 1;
//             a = a ^ b;
//             b = tmp;
//         }
//         return a;
//     }
// }

// optimized solution
// Time: O(1) Memory: O(1)
var getSum = function(a, b) {
    while (b !== 0) {
        const [ xor, carry ] = [ (a ^ b), ((a & b) << 1) ];

        a = xor;
        b = carry;
    }

    return a;
};