
Problem: Two Sum II - Input Array Is Sorted (LeetCode 167)
Approach: Two pointers (left & right)
Time Complexity: O(n)
Space Complexity: O(1)
Code:

def two_sum_ii(numbers, target):
    left, right = 0, len(numbers) - 1
    
    while left < right:
        total = numbers[left] + numbers[right]
        
        if total == target:
            return [left + 1, right + 1]  # 1-based index
        elif total < target:
            left += 1
        else:
            right -= 1
    
    return []



print(two_sum_ii([2, 7, 11, 15], 9))
