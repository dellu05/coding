"""Reversing directions
Chef recently printed directions from his home to a hot new restaurant across the town, but forgot to print the directions to get back home. Help Chef to transform the directions to get home from the restaurant.

A set of directions consists of several instructions. The first instruction is of the form "Begin on XXX", indicating the street that the route begins on. Each subsequent instruction is of the form "Left on XXX" or "Right on XXX", indicating a turn onto the specified road.

When reversing directions, all left turns become right turns and vice versa, and the order of roads and turns is reversed. See the sample input for examples.

Input
Input will begin with an integer T, the number of test cases that follow. Each test case begins with an integer N, the number of instructions in the route. N lines follow, each with exactly one instruction in the format described above.

Output
For each test case, print the directions of the reversed route, one instruction per line. Print a blank line after each test case.

Constraints
1 ≤ T ≤ 15
2 ≤ N ≤ 40
Each line in the input will contain at most 50 characters, will contain only alphanumeric characters and spaces and will not contain consecutive spaces nor trailing spaces. By alphanumeric characters we mean digits and letters of the English alphabet (lowercase and uppercase).
Sample 1:
Input
Output
2
4
Begin on Road A
Right on Road B
Right on Road C
Left on Road D
6
Begin on Old Madras Road
Left on Domlur Flyover
Left on 100 Feet Road
Right on Sarjapur Road
Right on Hosur Road
Right on Ganapathi Temple Road
Begin on Road D
Right on Road C
Left on Road B
Left on Road A
Begin on Ganapathi Temple Road
Left on Hosur Road
Left on Sarjapur Road
Left on 100 Feet Road
Right on Domlur Flyover
Right on Old Madras Road

Explanation:
In the first test case, the destination lies on Road D, hence the reversed route begins on Road D. The final turn in the original route is turning left from Road C onto Road D. The reverse of this, turning right from Road D onto Road C, is the first turn in the reversed route."""
# cook your dish here
import sys

def solve():
    # Input mothama read panrom
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    t_cases = int(input_data[0])
    current_line = 1
    
    for _ in range(t_cases):
        n = int(input_data[current_line])
        current_line += 1
        
        roads = []
        turns = []
        
        for i in range(n):
            line = input_data[current_line]
            current_line += 1
            
            # "Begin on ", "Left on ", "Right on " - idhula irundhu split panrom
            if line.startswith("Begin"):
                turns.append("Begin")
                roads.append(line[9:]) # "Begin on " (9 chars) thalli irukurathu road name
            elif line.startswith("Left"):
                turns.append("Left")
                roads.append(line[8:]) # "Left on " (8 chars)
            elif line.startswith("Right"):
                turns.append("Right")
                roads.append(line[9:]) # "Right on " (9 chars)

        # Reversing Logic:
        # 1. Last road thaan ippo "Begin on"
        print(f"Begin on {roads[-1]}")
        
        # 2. Matha roads-ku reverse turn apply pannanum
        # Forward-la i-th road-ku pona enna turn use pannangalo, 
        # return-la (i-1)-th road-ku poga adhoda opposite turn use pannanum.
        for i in range(n-1, 0, -1):
            original_turn = turns[i]
            # Swap: Left -> Right, Right -> Left
            reversed_turn = "Right" if original_turn == "Left" else "Left"
            print(f"{reversed_turn} on {roads[i-1]}")
        
        # Blank line after each test case
        print()

if __name__ == "__main__":
    solve()
