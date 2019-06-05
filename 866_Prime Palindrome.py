'''
Next smallest prime palindrome
Given a positive integer N where 1 \leq N \leq 10^{9}. The task is to find the smallest prime palindrome greater than or equal to N.

Examples:

Input: 8
Output: 11

Input: 7000000000
Output: 10000500001
Approach:

The Naive approach is to loop from N + 1 until we found next smallest prime palindrome greater than or equal to N.

Efficient Approach:
Lets say P = R is a the next smallest prime-palindrome greater than or equal to N.
Now since R is a palindrome, the first half of the digits of R can be used to determine R up-to two possibilities. Let k be the first half of the digits in R. For eg. if k = 123, then R = 12321 or R = 123321.

Thus we iterate through each k upto 105 and create the associated palindrome R, and check whether R is a prime or not.
Also we will handle the odd and even palindromes separately, and break when we fount our result.

Below is the implementation of above approach:

https://www.geeksforgeeks.org/next-smallest-prime-palindrome/

PH: not understand.
'''

# Python3 implementation of above approach 
import math 
  
# Function to check whether a number is prime 
def is_prime(n): 
    return n > 1 and all(n % d for d in range(2, int(math.sqrt(n)) + 1)) 
  
# function to generate next smallest prime palindrome 
def NextprimePalindrome(N): 
  
    for k in range(1, 10**6): 
  
        # Check for odd-length palindromes 
        s = str(k) 
        x = int(s + s[-2::-1])  # eg. s = '1234' to x = int('1234321') 
  
        if x >= N and is_prime(x): 
            return x 
  
        # Check for even-length palindromes 
        s = str(k) 
        x = int(s + s[-1::-1])  # eg. s = '1234' to x = int('12344321') 
  
        if x >= N and is_prime(x): 
            return x 
  
# Driver code 
N = 7000000000
  
# Function call to print answer 
print(NextprimePalindrome(N)) 
  
# This code is written by 
# Sanjit_Prasad 