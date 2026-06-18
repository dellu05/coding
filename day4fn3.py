""" F - Division or Subtraction  / 
Time Limit: 2 sec / Memory Limit: 1024 MiB

Score : 
600 points

Problem Statement
Given is a positive integer 
N.

We will choose an integer 
K between 
2 and 
N (inclusive), then we will repeat the operation below until 
N becomes less than 
K.

Operation: if 
K divides 
N, replace 
N with 
N/K; otherwise, replace 
N with 
N−K.
In how many choices of 
K will 
N become 
1 in the end?

Constraints
2≤N≤10 
12
 
N is an integer.
Input
Input is given from Standard Input in the following format:

N
Output
Print the number of choices of 
K in which 
N becomes 
1 in the end.

Sample Input 1
Copy
6
Sample Output 1
Copy
3
There are three choices of 
K in which 
N becomes 
1 in the end: 
2, 
5, and 
6.

In each of these choices, 
N will change as follows:

When 
K=2: 
6→3→1
When 
K=5: 
6→1
When 
K=6: 
6→1
Sample Input 2
Copy
3141
Sample Output 2
Copy
13
Sample Input 3
Copy
314159265358
Sample Output 3
Copy
9 """

import sys
import math

def get_divisors(n):
    """O(sqrt(N)) time-la divisors kandupudikka"""
    divs = []
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            divs.append(i)
            if i*i != n:
                divs.append(n // i)
    return divs

def solve():
    # Input-a eduthu integer-a mathrom
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    
    # K values duplicate aagama irukka set use panrom
    ans = set()
    
    # Case 1: K, N-ai vagukkum pothu (K is a divisor of N)
    # Kandupudicha ella divisors-ayum check panrom
    for k in get_divisors(n):
        if k < 2:
            continue
        temp = n
        # K-vaala evvalavu thadava divide panna mudiyumo panrom
        while temp % k == 0:
            temp //= k
        # Adhuku apuram varra remainder 1-a iruntha K valid
        if temp % k == 1:
            ans.add(k)
            
    # Case 2: K, N-ai vagukkama irukkum pothu (K is a divisor of N-1)
    # N-1 oda divisors ellame valid K values thaan
    for k in get_divisors(n - 1):
        if k < 2:
            continue
        # N-1 oda divisor-a iruntha kandippa GCD(N, K) = 1, 
        # so Case 1-oda overlap aagathu
        ans.add(k)
        
    # Moththa count-a print panrom
    print(len(ans))

if __name__ == "__main__":
    solve()
