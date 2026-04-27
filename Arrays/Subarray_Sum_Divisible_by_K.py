
Problem: Subarray Sum Divisible by K (LeetCode 974)
Approach: Prefix Sum + HashMap (remainder frequency)
Time Complexity: O(n)
Space Complexity: O(n)
Code:

class Solution:
    def subarraysDivByK(self, nums, k):
        prefix_sum = 0
        count = 0
        hashmap = {0: 1}  # remainder 0 seen once
        
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            
            # handle negative remainder
            if remainder < 0:
                remainder += k
            
            if remainder in hashmap:
                count += hashmap[remainder]
            
            hashmap[remainder] = hashmap.get(remainder, 0) + 1
        
        return count
