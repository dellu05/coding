"""C - Daydream  / 
Time Limit: 2 sec / Memory Limit: 256 MiB

Score : 
300 points

Problem Statement
You are given a string 
S consisting of lowercase English letters. Another string 
T is initially empty. Determine whether it is possible to obtain 
S=T by performing the following operation an arbitrary number of times:

Append one of the following at the end of 
T: dream, dreamer, erase and eraser.
Constraints
1≦∣S∣≦10 
5
 
S consists of lowercase English letters.
Input
The input is given from Standard Input in the following format:

S
Output
If it is possible to obtain 
S=T, print YES. Otherwise, print NO.

Sample Input 1
Copy
erasedream
Sample Output 1
Copy
YES
Append erase and dream at the end of 
T in this order, to obtain 
S=T.

Sample Input 2
Copy
dreameraser
Sample Output 2
Copy
YES
Append dream and eraser at the end of 
T in this order, to obtain 
S=T.

Sample Input 3
Copy
dreamerer
Sample Output 3
Copy
NO"""
import sys

def solve():
    # Read input string
    s = sys.stdin.read().strip()
    
    # Reverse the string
    s = s[::-1]
    
    # Reverse the target words
    words = ["maerd", "remaerd", "esare", "resare"]
    
    i = 0
    n = len(s)
    
    while i < n:
        match_found = False
        for word in words:
            # Check if the substring starting at i matches one of our words
            if s[i:i+len(word)] == word:
                i += len(word)
                match_found = True
                break
        
        # If no words matched at this position, it's impossible
        if not match_found:
            print("NO")
            return

    # If we reached the end of the string perfectly
    print("YES")

if __name__ == "__main__":
    solve()
