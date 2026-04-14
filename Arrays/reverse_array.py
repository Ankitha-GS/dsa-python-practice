
Problem: Reverse Array
Approach: Two pointers (swap from both ends)
Time Complexity: O(n)
Space Complexity: O(1)
Code:

def reverse_array(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr


print(reverse_array([1, 2, 3, 4, 5]))
