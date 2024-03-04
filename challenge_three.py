# Write a function solution that, given an integer N, returns a string of length N containing
# as many different lower-case letters ('a'-'z') as possible,
# in which each letter occurs an equal number of times.
import string

def solution(N):
    # Validate N is an innteger, and is bwtween 1 and 200,000
    if type(N) == int and 1 <= N <= 200000:
        # use string module to get a string of all alphabets in lowercase as well as their length
        lowercase_alphabet_string = string.ascii_lowercase
        base_value = len(lowercase_alphabet_string)
        # check if N is a modulus of our base_value
        if N % base_value == 0:
            repeat_times = int(N / base_value)
            produced_string = lowercase_alphabet_string * repeat_times
            print(''.join(sorted(produced_string)))
            # Return a sorted string that is readable, sorted returns a list, while join concatenates these sorted characters back into a single string
            return ''.join(sorted(produced_string))
        else:
            diff = N % base_value
            balance = N - diff
            repeat_times = int(balance / base_value)
            # Ensure numbers below 26 also have results
            if repeat_times == 0:
                produced_string = lowercase_alphabet_string[:diff]
                print(''.join(sorted(produced_string)))
            # Return a sorted string that is readable, sorted returns a list, while join concatenates these sorted characters back into a single string
                return ''.join(sorted(produced_string))
            else:
                produced_string = lowercase_alphabet_string * repeat_times + lowercase_alphabet_string[:diff]
                print(''.join(sorted(produced_string)))
            # Return a sorted string that is readable, sorted returns a list, while join concatenates these sorted characters back into a single string
                return ''.join(sorted(produced_string))

    else:
        raise ValueError("'N' has to be an integer between 1 and 200000")
    
# Test Cases
print(solution(3))
print(solution(52))
print(solution(30))
print(solution("A string"))
