"""
Problem: Longest Consecutive Sequence (LeetCode 128)
Approach: HashSet to achieve O(n)
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            # start of sequence
            if num - 1 not in num_set:
                current = num
                length = 1
                
                while current + 1 in num_set:
                    current += 1
                    length += 1
                
                longest = max(longest, length)
        
        return longest
