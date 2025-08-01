from collections import deque

def max_sliding_window(nums, k):
    if not nums: return []

    dq = deque()
    result = []

    for i in range(len(nums)):
        # Remove indices that are out of current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller values as they are useless
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Append max value to result (when window is ready)
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# Example Usage:
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print("Sliding Window Maximums:", max_sliding_window(nums, k))
