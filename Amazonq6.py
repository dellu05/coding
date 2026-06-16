""" Suppose there is a circle. There are N petrol pumps on that circle. You will be given two sets of
data.
1. The amount of petrol that every petrol pump has.
2. Distance from that petrol pump to the next petrol pump.
Find a starting point where the truck can start to get through the complete circle without exhausting
its petrol in between.
Note : Assume for 1 litre petrol, the truck can go 1 unit of distance.
Example 1:
Input:
N = 4

Petrol = 4 6 7 4
Distance = 6 5 3 5
Output: 1
Explanation: There are 4 petrol pumps with
amount of petrol and distance to next
petrol pump value pairs as {4, 6}, {6, 5},
{7, 3} and {4, 5}. The first point from
where truck can make a circular tour is
2nd petrol pump. Output in this case is 1
(index of 2nd petrol pump).
Expected Time Complexity: O(N)
Expected Auxiliary Space : O(1)
Constraints:
2 ≤ N ≤ 10000
1 ≤ petrol, distance ≤ 1000 """

# Petrol Pump Circular Tour

n = int(input("Enter number of petrol pumps: "))

print("Enter petrol at each pump:")
petrol = list(map(int, input().split()))

print("Enter distance to next pump:")
distance = list(map(int, input().split()))

start = 0
balance = 0
deficit = 0

for i in range(n):
    balance += petrol[i] - distance[i]

    if balance < 0:
        start = i + 1
        deficit += balance
        balance = 0

if balance + deficit >= 0:
    print("Output:", start)
else:
    print("Output: -1")
