// Leetcode 0374 - Guess Number Higher or Lower
// Easy - Binary Search
// We are playing the Guess Game. The game is as follows:
//
// I pick a number from 1 to n. You have to guess which number I picked.
//
// Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
//
// You call a pre-defined API int guess(int num), which returns three possible results:
//
//    -1: Your guess is higher than the number I picked (i.e. num > pick).
//    1: Your guess is lower than the number I picked (i.e. num < pick).
//    0: your guess is equal to the number I picked (i.e. num == pick).
//
// Return the number that I picked.
//
/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
*/

// need this for tester to run
int guess(int num);

// Binary Search Solution
int guessNumber(int n){
    int left = 1;
    int middle;
    int right = n;
    int guess_result;

    while (true) {
        // middle = (left + right) / 2; - won't work with large ints
	// below prevents integer overflow in C
        middle = left + ((right - left) / 2);
        guess_result = guess(middle);
        if (guess_result < 0) {
            right = middle - 1;
        }
        else if (guess_result > 0) {
            left = middle + 1;
        }
        else {
            break;
        }
    }
    return middle;
}
