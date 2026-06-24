# O(1) space: Reverse array in-place
def reverse_in_place(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap using temporary variable
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1

    return arr


# Only uses 3 variables (left, right, temp)
# Space: O(1) - independent of array size

print(reverse_in_place([7, 4, 6, 9, 2, 3]))
