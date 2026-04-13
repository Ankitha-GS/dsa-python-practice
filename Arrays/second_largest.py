
Problem: Second Largest Element
Time Complexity: O(n)
Space Complexity: O(1)
Code:

def second_largest(arr):
    first = second = float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    return second


print(second_largest([2, 5, 1, 7, 3]))
