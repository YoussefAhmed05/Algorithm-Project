def dutch_flag_sort(arr):
    Red, White, Blue = 0, 0, len(arr) - 1

    while White <= Blue:
        if arr[White] == 'R':
            arr[Red], arr[White] = arr[White], arr[Red]
            Red += 1
            White += 1
        elif arr[White] == 'W':
            White += 1
        elif arr[White] == 'B':
            arr[White], arr[Blue] = arr[Blue], arr[White]
            Blue -= 1


# Example
arr = ['W', 'R', 'B','B', 'R', 'W',]
dutch_flag_sort(arr)
print(arr)


