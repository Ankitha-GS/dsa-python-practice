
Problem: Remove Duplicates from Sorted Array
LeetCode: 26

Approach:
- Use two pointers
- pointer i tracks unique elements
- pointer j scans array

Time Complexity: O(n)
Space Complexity: O(1)
Code:

def remove_duplicates(nums):
    if not nums:
        return 0

    i = 0 

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1



nums = [1, 1, 2, 2, 3, 4, 4]
k = remove_duplicates(nums)

print("Unique count:", k)
print("Modified array:", nums[:k])
