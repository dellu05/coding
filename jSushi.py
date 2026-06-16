""" Problem Statement

There are
N dishes, numbered 1,2,…,N. Initially, for each i (1≤i≤N), Dish i has ai​ (

1≤ai​≤3) pieces of sushi on it.

Taro will perform the following operation repeatedly until all the pieces of sushi are eaten:

    Roll a die that shows the numbers 

1,2,…,N with equal probabilities, and let i be the outcome. If there are some pieces of sushi on Dish

    i, eat one of them; if there is none, do nothing.

Find the expected number of times the operation is performed before all the pieces of sushi are eaten.
Constraints

    All values in input are integers.

1≤N≤300

    1≤ai​≤3

Input

Input is given from Standard Input in the following format:

N

a1​ 

a2​ 

… 

aN​

Output

Print the expected number of times the operation is performed before all the pieces of sushi are eaten. The output is considered correct when the relative difference is not greater than

10−9.
Sample Input 1
Copy

3
1 1 1

Sample Output 1
Copy

5.5

The expected number of operations before the first piece of sushi is eaten, is
1. After that, the expected number of operations before the second sushi is eaten, is 1.5. After that, the expected number of operations before the third sushi is eaten, is 3. Thus, the expected total number of operations is

1+1.5+3=5.5.
Sample Input 2
Copy

1
3

Sample Output 2
Copy

3

Outputs such as 3.00, 3.000000003 and 2.999999997 will also be accepted.
Sample Input 3
Copy

2
1 2

Sample Output 3
Copy

4.5

Sample Input 4
Copy

10
1 3 2 3 3 2 3 2 1 3

Sample Output 4
Copy

54.48064457488221
 """

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    N = int(input_data)
    A = [int(x) for x in input_data[1:]]
    
    # Track our target state counts
    init_c1 = A.count(1)
    init_c2 = A.count(2)
    init_c3 = A.count(3)
    
    # Create two 2D tables instead of a massive 3D table
    dp_prev = [[0.0] * (N + 2) for _ in range(N + 2)]
    dp_curr = [[0.0] * (N + 2) for _ in range(N + 2)]
    
    # Outer loop for c3 (k)
    for k in range(N + 1):
        # Reset current layer for the new loop iteration
        for j in range(N + 1):
            for i in range(N + 1):
                dp_curr[i][j] = 0.0
                
        for j in range(N + 1 - k):
            for i in range(N + 1 - k - j):
                if i == 0 and j == 0 and k == 0:
                    continue  # Base Case remains 0.0
                
                total_active = i + j + k
                
                # Dependencies from the current k layer
                val_c1 = dp_curr[i - 1][j] if i > 0 else 0.0
                val_c2 = dp_curr[i + 1][j - 1] if j > 0 else 0.0
                
                # Dependency from the previous k-1 layer
                val_c3 = dp_prev[i][j + 1] if k > 0 else 0.0
                
                dp_curr[i][j] = (N + i * val_c1 + j * val_c2 + k * val_c3) / total_active
        
        # If we just finished calculating the layer containing our answer, break early
        if k == init_c3:
            print(f"{dp_curr[init_c1][init_c2]:.14f}")
            return
            
        # Move current layer to previous layer for the next iteration
        # Deep copy isn't needed; we can just swap or overwrite references
        dp_prev = [row[:] for row in dp_curr]

if __name__ == '__main__':
    solve()
