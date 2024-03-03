import math

#  Write a function given an array A consisting of N integers, returns the maximum sum of two numbers whose digits add up to an equal sum.
#  If there are no two numbers whose digits have an equal sum, the function should return -1.

def solution(A):
    # Validate the data is an Array
    if type(A) == list:
        # number of integers in array
        N = len(A)
        sum_of_digits = list()
        # create a list of the sum of the digits of each integer
        for i in A:
            digits = math.modf(i/10)
            second_digit = round(digits[0], 2) * 10
            first_digit = digits[1]
            sum_of_digits.append(int(second_digit+first_digit))
        print(sum_of_digits)
    
    # Validate whether we have two numbers whose digits have an equal sum else return -1
        if len(sum_of_digits) != len(set(sum_of_digits)):
            print("We Can Process this Array")
        else:
            return -1

    else:
        raise ValueError("A has to be a list.")

# Test Cases
# print(dir(int))
print(solution([51, 71, 17, 42]))
print(solution([42, 33, 60]))
print(solution([51, 32, 43]))
# print(solution("Just a string"))
# print(solution(1234))