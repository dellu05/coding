""" C - Colorful Leaderboard  / 
Time Limit: 2 sec / Memory Limit: 256 MiB

Score : 
300 points

Problem Statement
In AtCoder, a person who has participated in a contest receives a color, which corresponds to the person's rating as follows:

Rating 
1-
399 : gray
Rating 
400-
799 : brown
Rating 
800-
1199 : green
Rating 
1200-
1599 : cyan
Rating 
1600-
1999 : blue
Rating 
2000-
2399 : yellow
Rating 
2400-
2799 : orange
Rating 
2800-
3199 : red
Other than the above, a person whose rating is 
3200 or higher can freely pick his/her color, which can be one of the eight colors above or not.
Currently, there are 
N users who have participated in a contest in AtCoder, and the 
i-th user has a rating of 
a 
i
​
 .
Find the minimum and maximum possible numbers of different colors of the users.

Constraints
1≤N≤100
1≤a 
i
​
 ≤4800
a 
i
​
  is an integer.
Input
Input is given from Standard Input in the following format:

N
a 
1
​
  
a 
2
​
  
... 
a 
N
​
 
Output
Print the minimum possible number of different colors of the users, and the maximum possible number of different colors, with a space in between.

Sample Input 1
Copy
4
2100 2500 2700 2700
Sample Output 1
Copy
2 2
The user with rating 
2100 is "yellow", and the others are "orange". There are two different colors.

Sample Input 2
Copy
5
1100 1900 2800 3200 3200
Sample Output 2
Copy
3 5
The user with rating 
1100 is "green", the user with rating 
1900 is blue and the user with rating 
2800 is "red".
If the fourth user picks "red", and the fifth user picks "blue", there are three different colors. This is one possible scenario for the minimum number of colors.
If the fourth user picks "purple", and the fifth user picks "black", there are five different colors. This is one possible scenario for the maximum number of colors.

Sample Input 3
Copy
20
800 810 820 830 840 850 860 870 880 890 900 910 920 930 940 950 960 970 980 990
Sample Output 3
Copy
1 1
All the users are "green", and thus there is one color.

 """ 

import sys

def solve():
    # Input mothathaiyum ore variya eduthu split panrom
    # Idhu N matrum ella ratings-ayum oru list-la kooti vaikum
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    # Ratings list
    a = list(map(int, data[1:]))
    
    # Standard colors count (8 types)
    # Gray, Brown, Green, Cyan, Blue, Yellow, Orange, Red
    counts = [0] * 8
    wildcards = 0
    
    for x in a:
        if x < 400: counts[0] += 1
        elif x < 800: counts[1] += 1
        elif x < 1200: counts[2] += 1
        elif x < 1600: counts[3] += 1
        elif x < 2000: counts[4] += 1
        elif x < 2400: counts[5] += 1
        elif x < 2800: counts[6] += 1
        elif x < 3200: counts[7] += 1
        else:
            # Rating 3200 mela iruntha avanga wildcard users
            wildcards += 1
            
    # Ethana standard categories-la aalunga irukanga nu pakrom
    fixed_colors = 0
    for c in counts:
        if c > 0:
            fixed_colors += 1
            
    # MINIMUM Logic:
    # 1. Standard colors iruntha, wildcards antha color-laye sernthukalam. So min = fixed_colors.
    # 2. Ella ratings-um 3200 mela iruntha (fixed=0), ellarum ore color-a choose pannanum. So min = 1.
    if fixed_colors > 0:
        min_ans = fixed_colors
    else:
        min_ans = 1
        
    # MAXIMUM Logic:
    # Ovvoru wildcard user-um oru pudhu color-a choose panna mudiyum.
    max_ans = fixed_colors + wildcards
    
    # Answer-a space vittu print panrom
    print(min_ans, max_ans)

if __name__ == "__main__":
    solve()
