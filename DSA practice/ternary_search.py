def search(arr, l, r, num):
    if l > r:
        return -1  # Base case: number not found

    mid1 = l + (r - l) // 3
    mid2 = r - (r - l) // 3

    if num == arr[mid1]:
        return mid1
    if num == arr[mid2]:
        return mid2

    if num < arr[mid1]:
        return search(arr, l, mid1 - 1, num)
    elif num > arr[mid2]:
        return search(arr, mid2 + 1, r, num)
    else:
        return search(arr, mid1 + 1, mid2 - 1, num)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = 0  # Try changing this to test different values
l = 0
r = len(arr) - 1
result = search(arr, l, r, num)

if result == -1:
    print("Number not found")
else:
    print("Number found at index", result)
