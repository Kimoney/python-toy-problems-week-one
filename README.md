# Python Toy Problems - Week 1

## Challenge 1

There are N boxes (numbered from 0 to N−1) arranged in a row. The K-th box contains A[K] bricks.

In one move you can take one brick from some box and move it to a box next to it (on the left or on the right).

**challenge_one.py** returns the minimum number of moves needed to end up with exactly 10 bricks in every box.

### Function solution(A);

The Function **solution(A)** takes in one argument and validates the input. If it is not a list, **challenge_one.py** raises an error.

If A is an list A of N integers, **challenge_one.py** calculates and returns the **minimum number** of moves needed to end up with exactly 10 bricks in every box.

If this is not possible, the function **solution(A)** returns **−1**.

## Challenge 2

Given a list of integers, **challenge_two.py** returns the maximum sum of two numbers whose digits add up to an equal sum.

If there are no two numbers whose digits have an equal sum, the function should return -1.

### Function solution(A):

The Function **solution(A)** takes in one argument  and validates the input. If it is not a list, **challenge_one.py** raises an error.

If the input is a list, **solution(A)** creates a list of the sum of the digits of each integer and validates whether we have two numbers whose digits have an equal sum. 

If the list has two numbers whose digits have an equal sumtwo numbers whose digits have an equal sum, **solution(A)** iterates over the list, adding, comparing and updating the maximum sum. When the iiteration is done, **solution(A)** returns the maximum sum of two numbers whose digits add up to an equal sum.

If the list does not have any, **solution(A)** returns -1



## Author
**John Kimani**

## License
**MIT**