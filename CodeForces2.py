""" B. Tatar TV Show
Time limit: 2 seconds Memory limit: 256 megabytes
During the holidays, Egor came to visit his friend Dabir in the city of Kazan.
Out of boredom, Dabir and Egor came up with a new business idea: to make their
own TV show.
The format of the show is very simple: in each episode they invite a guest and
play a game with them on a binary string.
In today's episode, Egor and Dabir invited Arseniy (aka MAKAN) — the main
celebrity of Omsk. For the game, they chose a binary string s of length n and an
integer k.
Arseniy can make an unlimited number of moves. In one move, he can choose an
integer i (1 \le i \le n - k) and invert the characters at positions i and
i + k, that is, change 0 to 1 and 1 to 0.
For example, if s = 10110 and k = 2, then by choosing i = 2, Arseniy inverts the
characters at positions 2 and 4: [10110 \to 11100].
Arseniy wants to get the main prize — 1,000,000 tugriks. To do this, he needs to
make the entire string s equal to zero.
Help Arseniy determine whether he can get his prize, or if he will have to
return to Omsk with nothing.
Input
The first line contains a single integer t (1 \le t \le 10^4) — the number of
test cases.
The first line of each test case contains two integers n and k
(1 \le k \le n \le 2 \cdot 10^5).
The second line of each test case contains a binary string s of length n.
It is guaranteed that the sum of n over all test cases does not exceed
2 \cdot 10^5.
Output
For each test case, output "YES" if Arseniy can make the string entirely zero,
and "NO" otherwise.
You can output "YES" and "NO" in any case (for example, "yEs", "yes", and "Yes"
will be accepted).
Example
Input:
5
4 2
1010
3 2
111
3 3
111
3 1
110
1 1
1
Output:
YES
NO
NO
YES
NO

 """
def solve():
    inp = input().split()
    if not inp:
        return
    
    t = int(inp[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(inp[idx])
        k = int(inp[idx + 1])
        s = inp[idx + 2]
        idx += 3
        
        possible = True
        # Check parity of 1s for each residue class modulo k
        for r in range(k):
            count_ones = 0
            # Step through the string at intervals of k
            for i in range(r, n, k):
                if s[i] == '1':
                    count_ones += 1
            
            # If any group has an odd number of 1s, it's impossible
            if count_ones % 2 != 0:
                possible = False
                break
        
        if possible:
            results.append("YES")
        else:
            results.append("NO")
            
    print("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
