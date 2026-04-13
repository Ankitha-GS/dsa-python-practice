
Problem: Find Minimum Element
Time Complexity: O(n)
Space Complexity: O(1)
Code:
def find_min(arr):
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val


print(find_min([2, 5, 1, 7, 3]))
