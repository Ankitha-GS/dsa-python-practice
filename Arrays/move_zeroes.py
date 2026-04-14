
Problem: Move Zeroes (LeetCode 283)
Approach: Two pointers (slow-fast)
Time Complexity: O(n)
Space Complexity: O(1)
Code:

def move_zeroes(nums):
    j = 0  
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    
    return nums



print(move_zeroes([0, 1, 0, 3, 12]))
