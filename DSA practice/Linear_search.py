def search(arr, num):
    for i in range(0, len(arr) - 1):
        if arr[i] == num:
            return i
    return -1

arr = [4, 6, 8, 10, 2, 12]
num = int(input("Enter number to find in array: "))
result = search(arr, num)
if result == -1:
    print("Number is not found...")
else: 
    print("Number is found at index of ", result)