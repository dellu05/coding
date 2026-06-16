""" Problem Statement

There are
N stones, numbered 1,2,…,N. For each i (1≤i≤N), the height of Stone i is

hi​.

There is a frog who is initially on Stone
1. He will repeat the following action some number of times to reach Stone

N:

    If the frog is currently on Stone 

i, jump to one of the following: Stone i+1,i+2,…,i+K. Here, a cost of ∣hi​−hj​∣ is incurred, where

    j is the stone to land on.

Find the minimum possible total cost incurred before the frog reaches Stone

N.
Constraints

    All values in input are integers.

2≤N≤105
1≤K≤100

    1≤hi​≤104

Input

Input is given from Standard Input in the following format:

N 

K

h1​ 

h2​ 

… 

hN​

Output

Print the minimum possible total cost incurred.
Sample Input 1
Copy

5 3
10 30 40 50 20

Sample Output 1
Copy

30

If we follow the path
1 → 2 → 5, the total cost incurred would be

∣10−30∣+∣30−20∣=30.
Sample Input 2
Copy

3 1
10 20 10

Sample Output 2
Copy

20

If we follow the path
1 → 2 → 3, the total cost incurred would be

∣10−20∣+∣20−10∣=20.
Sample Input 3
Copy

2 100
10 10

Sample Output 3
Copy

0

If we follow the path
1 → 2, the total cost incurred would be

∣10−10∣=0.
Sample Input 4
Copy

10 4
40 10 20 70 80 10 20 70 80 60

Sample Output 4
Copy

40

If we follow the path
1 → 4 → 8 → 10, the total cost incurred would be ∣40−70∣+∣70−70∣+∣70−60∣=40. """  
import sys

def solve():
    # Fast I/O configuration
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    N = int(input_data[0])
    K = int(input_data[1])
    h = [int(x) for x in input_data[2:]]
    
    # Initialize DP array with an upper bound infinity value
    INF = float('inf')
    dp = [INF] * N
    dp[0] = 0  # Starting point cost is 0
    
    # Compute the minimum cost for each stone sequentially
    for i in range(1, N):
        # Look back up to K stones, ensuring we don't go past index 0
        start_lookback = max(0, i - K)
        
        for j in range(start_lookback, i):
            cost = dp[j] + abs(h[i] - h[j])
            if cost < dp[i]:
                dp[i] = cost
                
    # The last element holds the ultimate minimum cost
    print(dp[N - 1])

if __name__ == '__main__':
    solve()
