
Problem: Longest Repeating Character Replacement (LeetCode 424)
Approach: Sliding Window + Frequency Map
Time Complexity: O(n)
Space Complexity: O(1)
Code:

class Solution:
    def characterReplacement(self, s, k):
        count = {}
        left = 0
        maxf = 0
        res = 0
        
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxf = max(maxf, count[s[right]])
            
            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res
