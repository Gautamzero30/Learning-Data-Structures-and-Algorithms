def min_swaps_to_group_k(arr, k):
    n = len(arr)

    # Step 1: Count total number of 1's in array
    total_ones = arr.count(1)
    if total_ones == 0 or total_ones == 1:
        return 0  # already grouped

    # Step 2: We only need a window size equal to total_ones
    window_size = total_ones

    # Step 3: Count number of 1's in the first window
    current_ones = sum(arr[:window_size])

    # Step 4: Use sliding window to find max_ones in any window of size window_size
    max_ones_in_window = current_ones
    for i in range(window_size, n):
        current_ones += arr[i] - arr[i - window_size]
        max_ones_in_window = max(max_ones_in_window, current_ones)

    # Step 5: The minimum swaps = window size - max_ones_in_window
    return window_size - max_ones_in_window


# Example
arr = [1, 0, 1, 0, 1]
k = 3
print("Minimum swaps needed:", min_swaps_to_group_k(arr, k))
