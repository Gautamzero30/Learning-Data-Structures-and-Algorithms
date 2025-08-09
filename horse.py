def can_place(stalls, k, dist):
    count = 1  # first horse in first stall
    last_position = stalls[0]

    for pos in stalls[1:]:
        if pos - last_position >= dist:
            count += 1
            last_position = pos
            if count == k:
                return True
    return False

def max_min_distance(stalls, k):
    stalls.sort()
    low = 1
    high = stalls[-1] - stalls[0]
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if can_place(stalls, k, mid):
            result = mid
            low = mid + 1  # try for bigger distance
        else:
            high = mid - 1  # try for smaller distance
    return result

# Example usage
stalls = [1, 2, 8, 4, 9]
k = 3
print("Max possible minimum distance:", max_min_distance(stalls, k))
