def merge_sort(arr):
    """
    Sort an array using the Merge Sort algorithm.
    Time Complexity: O(n log n) - all cases
    Space Complexity: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    """Merge two sorted arrays into one sorted array."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


# Test with the given list
arr = [45, 12, 3, 67, 34, 21]
print(f"Original list: {arr}")
sorted_arr = merge_sort(arr)
print(f"Sorted list: {sorted_arr}")