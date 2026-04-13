
Problem: Linear Search
Time Complexity: O(n)
Space Complexity: O(1)
Code:

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


print(linear_search([2, 5, 1, 7, 3], 7))
