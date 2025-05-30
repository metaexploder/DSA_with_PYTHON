def binary_search(arr, i, j, num):
    if i > j:
        return -1  # base case
    
    mid = (i + j) // 2
    if arr[mid] == num:
        return mid
    elif arr[mid] < num:
        return binary_search(arr, mid + 1, j, num)
    else:
        return binary_search(arr, i, mid - 1, num)

arr = [1, 2, 3, 4, 5, 6] #condition for binary search that array must be sorted
i = 0
j = len(arr) - 1  # Fix: use len(arr) - 1
num = int(input("Enter number to find in array: "))
result = binary_search(arr, i, j, num)

if result == -1:
    print("Number is not found...")
else:
    print("Number is found at index", result)





# def binary_search(arr, i, j, num):
#     mid = (i + j)  // 2
#     if arr[mid] == num:
#         return mid
#     elif arr[mid] < num:
#         return binary_search(arr, mid + 1, j, num)
#     else:
#         return binary_search(arr, i, mid - 1, num)
#     return - 1


# arr = [1, 2, 3, 4, 5, 6]
# j = len(arr) 
# i= 0
# num = int(input("Enter number to find in array: "))
# result = binary_search(arr, i, j, num)
# if result == -1:
#     print("Number is not found...")
# else: 
#     print("Number is found at index of ", result)