"""D - Integer Cards  / 
Time Limit: 2 sec / Memory Limit: 1024 MiB

Score : 
400 points

Problem Statement
You have 
N cards. On the 
i-th card, an integer 
A 
i
​
  is written.

For each 
j=1,2,...,M in this order, you will perform the following operation once:

Operation: Choose at most 
B 
j
​
  cards (possibly zero). Replace the integer written on each chosen card with 
C 
j
​
 .

Find the maximum possible sum of the integers written on the 
N cards after the 
M operations.

Constraints
All values in input are integers.
1≤N≤10 
5
 
1≤M≤10 
5
 
1≤A 
i
​
 ,C 
i
​
 ≤10 
9
 
1≤B 
i
​
 ≤N
Input
Input is given from Standard Input in the following format:

N 
M
A 
1
​
  
A 
2
​
  
... 
A 
N
​
 
B 
1
​
  
C 
1
​
 
B 
2
​
  
C 
2
​
 
⋮
B 
M
​
  
C 
M
​
 
Output
Print the maximum possible sum of the integers written on the 
N cards after the 
M operations.

Sample Input 1
Copy
3 2
5 1 4
2 3
1 5
Sample Output 1
Copy
14
By replacing the integer on the second card with 
5, the sum of the integers written on the three cards becomes 
5+5+4=14, which is the maximum result.

Sample Input 2
Copy
10 3
1 8 5 7 100 4 52 33 13 5
3 10
4 30
1 4
Sample Output 2
Copy
338
Sample Input 3
Copy
3 2
100 100 100
3 99
3 99
Sample Output 3
Copy
300
Sample Input 4
Copy
11 3
1 1 1 1 1 1 1 1 1 1 1
3 1000000000
4 1000000000
3 1000000000
Sample Output 4
Copy
10000000001
The output may not fit into a 
32-bit integer type."""
import sys

def solve():
    # Fast Input reading
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    # Card values
    A = list(map(int, input_data[2:2+N]))
    A.sort() # Step 1: Smallest to largest
    
    # Operations: (value C, count B)
    ops = []
    curr = 2 + N
    for _ in range(M):
        b = int(input_data[curr])
        c = int(input_data[curr+1])
        ops.append((c, b))
        curr += 2
    
    # Step 2: Largest replacement value first
    ops.sort(key=lambda x: x[0], reverse=True)
    
    # Step 3: Greedy Replacement
    a_ptr = 0
    for val, count in ops:
        # Replace up to 'count' cards
        for _ in range(count):
            if a_ptr < N and A[a_ptr] < val:
                A[a_ptr] = val
                a_ptr += 1
            else:
                # If current card >= replacement, no more replacements needed
                print(sum(A))
                return
        if a_ptr >= N:
            break
            
    print(sum(A))

solve()
