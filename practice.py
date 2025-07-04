# def wordPattern(pattern, s):
    
#     lst_of_words = s.split(" ")
#     lst_of_chars = [char for char in pattern]
#     if len(list(set(lst_of_words))) == len(list(set(pattern))) and len(lst_of_chars) == len(lst_of_words):
#         pairs = list(zip(lst_of_chars, lst_of_words))
#         if len(list(set(pairs))) != len(list(set(pattern))):
#             return False
#         return True
#     return False

# pattern = "abba"
# s = "dog do do dog"
# print(wordPattern(pattern, s))




# n = int(input("Enter range: "))

# a, b = 0, 1
# print(f"Fibonacci Series upto {n} numbers: ", end='')
# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b





#PRIME NUMBER UPTO GIVEN NUMBER
# import time

# n = int(input("Enter number till you want prime numbers: "))

# start = time.time()  # Start time

# for num in range(2, n + 1):
#     flag = 0
#     for check in range(2, num // 2 + 1):
#         if num % check == 0:
#             flag = 1
#             break
#     if flag == 0:
#         print(num, end=', ')

# end = time.time()  # End time

# print(f"\nExecution Time: {end - start:.6f} seconds")
# execution_time_ms = (end - start) * 1000  # Convert to milliseconds

# print(f"Execution Time: {execution_time_ms:.3f} ms")


#optimized version of prime number
import math
import time
n = int(input("Enter : "))
start = time.time()
print(2, end=', ')
for num in range(3, n + 1, 2):  # Skip even numbers
    is_prime = True
    for check in range(3, int(math.sqrt(num)) + 1, 2):
        if num % check == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=', ')

end = time.time()
print(f"\nExecution time : {end - start:.6f} seconds")
