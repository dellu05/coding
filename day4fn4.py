""" D - XOR World  / 
Time Limit: 2 sec / Memory Limit: 1024 MiB

Score : 
400 points

Problem Statement
Let 
f(A,B) be the exclusive OR of 
A,A+1,...,B. Find 
f(A,B).

What is exclusive OR?
Constraints
All values in input are integers.
0≤A≤B≤10 
12
 
Input
Input is given from Standard Input in the following format:

A 
B
Output
Compute 
f(A,B) and print it.

Sample Input 1
Copy
2 4
Sample Output 1
Copy
5
2,3,4 are 010, 011, 100 in base two, respectively. The exclusive OR of these is 101, which is 
5 in base ten.

Sample Input 2
Copy
123 456
Sample Output 2
Copy
435
Sample Input 3
Copy
123456789012 123456789012
Sample Output 3
Copy
123456789012
 """

import sys

def get_xor_zero_to_n(n):
    """0 முதல் n வரை உள்ள எண்களின் XOR பலனை O(1)-ல் தரும்"""
    if n < 0:
        return 0
    
    remainder = n % 4
    if remainder == 0:
        return n
    elif remainder == 1:
        return 1
    elif remainder == 2:
        return n + 1
    else: # remainder == 3
        return 0

def solve():
    # Input-ஐ படிக்கிறோம்
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    a = int(input_data[0])
    b = int(input_data[1])
    
    # f(A, B) = g(B) XOR g(A-1)
    ans = get_xor_zero_to_n(b) ^ get_xor_zero_to_n(a - 1)
    
    print(ans)

if __name__ == "__main__":
    solve()
