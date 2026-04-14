
Problem: Valid Palindrome (LeetCode 125)
Approach: Two pointers from both ends
Time Complexity: O(n)
Space Complexity: O(1)
Code:
def is_palindrome(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    
    return True
