#  Write a function given an array A consisting of N integers, returns the maximum sum of two numbers whose digits add up to an equal sum.
#  If there are no two numbers whose digits have an equal sum, the function should return -1.
def solution(A):
    # Validate the data is an Array
    if type(A) == list:
        pass
    else:
        raise ValueError("A has to be a list.")

# Test Cases
print(solution([51, 71, 17, 42]))
print(solution([42, 33, 60]))
print(solution([51, 32, 43]))
print(solution("Just a string"))
print(solution(1234))