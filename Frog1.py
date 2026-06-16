""" Problem Statement

There are
N stones, numbered 1,2,…,N. For each i (1≤i≤N), the height of Stone i is

hi​.

There is a frog who is initially on Stone
1. He will repeat the following action some number of times to reach Stone

N:

    If the frog is currently on Stone 

i, jump to Stone i+1 or Stone i+2. Here, a cost of ∣hi​−hj​∣ is incurred, where

    j is the stone to land on.

Find the minimum possible total cost incurred before the frog reaches Stone

N.
Constraints

    All values in input are integers.

2≤N≤105

    1≤hi​≤104

Input

Input is given from Standard Input in the following format:

N

h1​ 

h2​ 

… 

hN​

Output

Print the minimum possible total cost incurred.
Sample Input 1
Copy

4
10 30 40 20

Sample Output 1
Copy

30

If we follow the path
1 → 2 → 4, the total cost incurred would be

∣10−30∣+∣30−20∣=30.
Sample Input 2
Copy

2
10 10

Sample Output 2
Copy

0

If we follow the path
1 → 2, the total cost incurred would be

∣10−10∣=0.
Sample Input 3
Copy

6
30 10 60 10 60 50

Sample Output 3
Copy

40

If we follow the path
1 → 3 → 5 → 6, the total cost incurred would be ∣30−60∣+∣60−60∣+∣60−50∣=40. """

import sys

def solve():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    N = int(input_data[0])
    h = [int(x) for x in input_data[1:]]
    
    # Handle the minimal base case scenario
    if N == 2:
        print(abs(h[1] - h[0]))
        return

    # Initialize DP table
    dp = [0] * N
    dp[0] = 0
    dp[1] = abs(h[1] - h[0])
    
    # Populate the DP table using the transition relation
    for i in range(2, N):
        jump_one = dp[i - 1] + abs(h[i] - h[i - 1])
        jump_two = dp[i - 2] + abs(h[i] - h[i - 2])
        dp[i] = min(jump_one, jump_two)
        
    # The last element holds the minimum cost to reach Stone N
    print(dp[N - 1])

if __name__ == '__main__':
    solve()
