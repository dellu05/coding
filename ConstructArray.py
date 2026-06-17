
""" A. Construct an Array

Time limit: 1 second Memory limit: 256 megabytes

You are given an integer n. You need to construct an array of integers
a_1, a_2, \dots, a_n such that the following conditions are satisfied:

  - 1 \le a_i \le 2 \cdot n for all i from 1 to n.
  - All elements of the array and the sums of adjacent elements are pairwise
    distinct. In other words, among the numbers
    \{a_1, a_2, \dots, a_n, a_1 + a_2, a_2 + a_3, \dots, a_{n-1} + a_n\}, there
    should not be two equal numbers.

Input

Each test contains multiple test cases. The first line contains the number of
test cases t (1 \le t \le 100). The description of the test cases follows.

The only line of each test case contains one integer n (1 \le n \le 500).

Output

For each test case, output an array of length n that satisfies the condition of
the problem. It can be shown that such an array always exists under the given
constraints.

If there are multiple solutions, you can output any of them.

Example

Input:

3
1
3
6

Output:

1
6 2 3
8 1 11 2 3 4

(Note: Your output using the odd numbers logic 1 3 5... is also a perfectly
valid answer and will be accepted.)

Note

  - In the second example (n=3), the array is [6, 2, 3]. All elements and
    adjacent sums form the set \{6, 2, 3, 8, 5\}, all of whose elements are
    distinct.
  - In the third example (n=6), the array is [8, 1, 11, 2, 3, 4]. All elements
    and adjacent sums form the set \{8, 1, 11, 2, 3, 4, 9, 12, 13, 5, 7\}, whose
    elements are also distinct.
"""

def solve():
    
    input_data = input().split()
    if not input_data:
        return
    t = int(input_data[0])
    pointer = 1
    
    results = []
    for _ in range(t):
        if pointer >= len(input_data):
            break
        n = int(input_data[pointer])
        pointer += 1
        arr = []
        for i in range(1, n + 1):
            arr.append(str(2 * i - 1))
        
        results.append(" ".join(arr))
    
    print("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
