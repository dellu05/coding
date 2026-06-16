"""Emergency Drone Corridor
Scenario
A coastal city uses autonomous drones to deliver emergency medical supplies after a cyclone. Along a straight evacuation corridor, several buildings of different heights exist.
After heavy rainfall, drones can only fly through air pockets formed between taller buildings. The amount of usable airspace above a building depends on the tallest building to its left and right.
Your task is to calculate the total navigable airspace available for drones.
Input
An array heights[] of n non-negative integers where:
    • heights[i] represents the height of the i-th building. 
    • Width of each building is 1 unit.
Output
    • Return the total volume of navigable airspace.


Example 1
Input:
heights = [0,1,0,2,1,0,1,3,2,1,2,1]
Output:
6
Example 2
Input:
heights = [4,2,0,3,2,5]
Output:
9
Constraints
1 <= n <= 10^7
0 <= heights[i] <= 10^9
Challenge
A naive solution will exceed the time limit.
Expected Complexity
Time: O(n)
Space: O(1)
Disallowed
O(n²)
O(n) extra arrays
Hidden Test Cases
Students often fail on:
[5,4,3,2,1]
[1,2,3,4,5]
[5,0,0,0,5]
[1000000000,0,1000000000]
 """
def calculate_navigable_airspace(heights):
    if len(heights) == 0:
        return 0
    number_of_buildings = len(heights)
    left = 0
    right = number_of_buildings - 1
    tallest_on_left = heights[left]
    tallest_on_right = heights[right]
    total_airspace = 0
    while left < right:
        if tallest_on_left < tallest_on_right:
            left += 1
            tallest_on_left = max(tallest_on_left, heights[left])
            total_airspace += tallest_on_left - heights[left]
        else:
            right -= 1
            tallest_on_right = max(tallest_on_right, heights[right])
            total_airspace += tallest_on_right - heights[right]
    return total_airspace
buildings = [0,1,0,2,1,0,1,3,2,1,2,1]
result = calculate_navigable_airspace(buildings)
print("Total Navigable Airspace =", result)

#solution
def airspace(h):
    l,r,lm,rm,ans=0,len(h)-1,0,0,0
    while l<r:
        if h[l]<h[r]:
            lm=max(lm,h[l]);ans+=lm-h[l];l+=1
        else:
            rm=max(rm,h[r]);ans+=rm-h[r];r-=1
    return ans

Time Complexity : O(n)
Space Complexity: O(1)
LOC inside function: ≤ 8

