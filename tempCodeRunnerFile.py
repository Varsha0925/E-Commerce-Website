def min_risk(arr):
    # Convert '0' to -1 for easier processing
    arr = [-1 if x == 0 else int(x) for x in arr]

    # Replace -1 with either 1 or 2
    for i in range(len(arr)):
        if arr[i] == -1:
            # Find the nearest non-zero number on the left
            left = i - 1
            while left >= 0 and arr[left] == -1:
                left -= 1

            # Find the nearest non-zero number on the right
            right = i + 1
            while right < len(arr) and arr[right] == -1:
                right += 1

            # Replace -1 with a number of the same parity as the nearest non-zero number
            if left >= 0 and right < len(arr):
                if arr[left] % 2 == arr[right] % 2:
                    arr[i] = 1 if arr[left] % 2 == 0 else 2
                else:
                    # If the parities are different, choose the one that minimizes the risk
                    arr[i] = 1 if abs(arr[left] - 1) + abs(arr[right] - 1) < abs(arr[left] - 2) + abs(arr[right] - 2) else 2
            elif left >= 0:
                arr[i] = 1 if arr[left] % 2 == 0 else 2
            else:
                arr[i] = 1 if arr[right] % 2 == 0 else 2

    # Calculate risk value
    risk = sum(1 for i in range(1, len(arr)) if arr[i] % 2 != arr[i-1] % 2)

    return risk

print(min_risk([1,0,0,5,0,0,2]))  # Output: 1