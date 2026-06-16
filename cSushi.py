""" Problem Statement
There are
N pieces of shari (vinegared rice) and
M pieces of neta (toppings) as ingredients for sushi.
The weight of the
i-th shari is Ai​, and the weight of the j-th neta is Bj​.
You will make sushi by combining shari and neta.
To make one piece of sushi, you need to combine one shari with one neta. Here, the weight of the neta must be at most twice the weight of the shari. Also, the same shari or neta cannot be used in multiple pieces of sushi.
Find the maximum number of sushi that can be made.
Constraints
1≤N,M≤2×105
1≤Ai​,Bj​≤109
All input values are integers.

Input
The input is given from Standard Input in the following format:
N M
A1​ A2​ … AN​
B1​ B2​ … BM​

Output
Output the answer.
Sample Input 1
4 5
4 2 1 8
14 9 3 2 9

Sample Output 1
3
By combining the
1st shari with the 3rd neta, the 2nd shari with the 4th neta, and the 4th shari with the 1st neta, for example, you can make three pieces of sushi. It is impossible to make four or more pieces of sushi, so output
3.
Sample Input 2
3 3
5 5 3
11 1000 1000

Sample Output 2
0
Sample Input 3
8 7
2 3 4 4 4 3 2 3
8 5 5 9 9 7 1

Sample Output 3
5
"""

data=input().split()
n=int(data[0])
m=int(data[1])
a=[int(x) for x in data[2:2+n]]
b=[int(x) for x in data[2+n:2+n+m]]
a.sort()
b.sort()
si=0
ni=0
sc=0
while si<n and ni<m:
    if b[ni]<=2*a[si]:
        si+=1
        ni+=1
        sc+=1
    else:
        si+=1
print(sc)
