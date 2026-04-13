
Problem: Find Maximum Element
Time Complexity: O(n)
Space Complexity: O(1)

def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val
