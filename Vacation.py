""" Problem Statement

Taro's summer vacation starts tomorrow, and he has decided to make plans for it now.

The vacation consists of
N days. For each i (1≤i≤N), Taro will choose one of the following activities and do it on the

i-th day:

    A: Swim in the sea. Gain 

ai​ points of happiness.
B: Catch bugs in the mountains. Gain
bi​ points of happiness.
C: Do homework at home. Gain

    ci​ points of happiness.

As Taro gets bored easily, he cannot do the same activities for two or more consecutive days.

Find the maximum possible total points of happiness that Taro gains.
Constraints

    All values in input are integers.

1≤N≤105

    1≤ai​,bi​,ci​≤104

Input

Input is given from Standard Input in the following format:

N

a1​ 

b1​ 

c1​

a2​ 

b2​ 

c2​

:

aN​ 

bN​ 

cN​

Output

Print the maximum possible total points of happiness that Taro gains.
Sample Input 1
Copy

3
10 40 70
20 50 80
30 60 90

Sample Output 1
Copy

210

If Taro does activities in the order C, B, C, he will gain

70+50+90=210 points of happiness.
Sample Input 2
Copy

1
100 10 1

Sample Output 2
Copy

100

Sample Input 3
Copy

7
6 7 8
8 8 3
2 5 2
7 8 6
4 6 8
2 3 4
7 5 1

Sample Output 3
Copy

46

Taro should do activities in the order C, A, B, A, C, B, A. """
import sys

def solve():
    # Read all inputs efficiently from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    N = int(input_data[0])
    
    # Base cases for day 1
    dp_a = int(input_data[1])
    dp_b = int(input_data[2])
    dp_c = int(input_data[3])
    
    # Process days 2 to N
    idx = 4
    for _ in range(1, N):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        
        # Calculate new max states based on non-consecutive choices
        next_a = a + max(dp_b, dp_c)
        next_b = b + max(dp_a, dp_c)
        next_c = c + max(dp_a, dp_b)
        
        # Shift the row states forward
        dp_a, dp_b, dp_c = next_a, next_b, next_c
        
    # The final answer is the maximum among the three paths on the last day
    print(max(dp_a, dp_b, dp_c))

if __name__ == '__main__':
    solve()
