# Given an array A of N integers, the function solution returns
# the minimum number of moves needed to end up with exactly 10 bricks in every box.
# If this is not possible, the function should return −1.

def solution(A):
    # Validate the data type and whether the sum of all integers is a multiple of 10 to ensure we end up with exactly 10 bricks in every box
    if (type(A) == list and sum(A) % 10 == 0):
        
         # Get the number of integers on the Array
        N = len(A)
        desired_bricks = 10
        moves = 0

        # Create the array need_or_excess that hold the needed or excessive bricks per box
        need_or_excess = [A[i] - desired_bricks for i in range(N)]
        print(need_or_excess)
        # Iterate over the need_or_excess list and determine how to move the boxes
        for i in range(N-1):
            # shift bricks to the right
            if need_or_excess[i] < 0:
                moves += abs(need_or_excess[i])
                need_or_excess[i+1] += need_or_excess[i]
                need_or_excess[i] = 0
            # shift bricks to the left
            elif need_or_excess[i] > 0:
                moves += need_or_excess[i]
                need_or_excess[i+1] += need_or_excess[i]
                need_or_excess[i] = 0

        # Output the updated moves
        return moves
    else:
        print(-1)

print(solution([7, 15, 10, 8]))
print(solution([11, 10, 8, 12, 8, 10, 11]))
print(solution([7, 14, 10]))
print(solution(123))