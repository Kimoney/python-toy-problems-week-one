# Given an array A of N integers, the function solution returns
# the minimum number of moves needed to end up with exactly 10 bricks in every box.
# If this is not possible, the function should return −1.

def solution(A):
    # Check whether the sum of all integers is a multiple of 10 to ensure we end up with exactly 10 bricks in every box
    if (type(A) == list and sum(A) % 10 == 0):
        print("okay")
    else:
        print(-1)

solution([7, 15, 10, 8])