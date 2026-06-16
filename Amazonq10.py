"""Given two strings s and t. Return the minimum number of operations required to convert s to t.
The possible operations are permitted:
1. Insert a character at any position of the string.
2. Remove any character from the string.
3. Replace any character from the string with any other character.

Example 1:
Input:
s = "geek", t = "gesek"
Output: 1
Explanation: One operation is required
inserting 's' between two 'e's of str1.
Example 2:
Input :
s = "gfg", t = "gfg"
Output:
0
Explanation: Both strings are same.
Expected Time Complexity: O(|s|*|t|)
Expected Space Complexity: O(|s|*|t|)
Constraints:
1 ≤ Length of both strings ≤ 100
Both the strings are in lowercase.
"""
# Edit Distance

s = input("Enter first string: ")
t = input("Enter second string: ")

m = len(s)
n = len(t)

dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

# Fill first row and first column
for i in range(m + 1):
    dp[i][0] = i

for j in range(n + 1):
    dp[0][j] = j

# Fill DP table
for i in range(1, m + 1):
    for j in range(1, n + 1):

        if s[i - 1] == t[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]

        else:
            dp[i][j] = 1 + min(
                dp[i - 1][j],      # Remove
                dp[i][j - 1],      # Insert
                dp[i - 1][j - 1]   # Replace
            )

print("Minimum Operations =", dp[m][n])
