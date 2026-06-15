"""Given a string S, find the length of the longest substring without repeating characters.
Example 1:
Input:
S = "geeksforgeeks"
Output:
7
Explanation:
Longest substring is
"eksforg".
Example 2:
Input:
S = "abdefgabef"
Output:
6
Explanation:
Longest substring are
"abdefg" , "bdefga" and "defgab".
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(K) where K is constant
Constraints:
1 ≤ |S| ≤ 105
It is guaranteed that all characters of the String S will be lowercase letters from 'a' to 'z'"""

def longest_unique_substring(s):
    seen = {}
    max_len = 0
    start = 0
    for end in range(len(s)):
        char = s[end]
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = end
        max_len = max(max_len, end - start + 1)
     return max_len
if __name__ == "__main__":
    user_input = input("Enter string S: ")
    result = longest_unique_substring(user_input)
    print(f"Output: {result}")
