def max_subarray(numbers):
    """Find the largest sum of any contiguous subarray."""
    best_sum = 0  # Declare the best sum
    current_sum = 0  # Declare current sum
    for x in numbers:  # For each of the numbers in the list
        current_sum = max(0, current_sum + x)  # The current sum is equal to either zero or x, whichever is larger
        best_sum = max(best_sum,
                       current_sum)  # The best sum is the largest of the previous best sum and the current sum
    return best_sum


def max_no_empty(nums):
    if not nums:
        raise ValueError("Array is empty")
    best_sum = nums[0]
    current_sum = 0
    for x in nums:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum
