# Write a function solution that, given an integer N, returns a string of length N containing
# as many different lower-case letters ('a'-'z') as possible,
# in which each letter occurs an equal number of times.
import string

def solution(N):
    # Validate N is an innteger, and is bwtween 1 and 200,000
    if type(N) == int and 1 <= N <= 200000:
        # use string module to get a string of all alphabets in lowercase
        lowercase_alphabet_string = string.ascii_lowercase
        
    else:
        raise ValueError("'N' has to be an integer between 1 and 200000")
    
# Test Cases
print(solution(3))
print(solution(5))
print(solution(30))
print(solution("A string"))
