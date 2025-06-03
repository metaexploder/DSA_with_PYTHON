class Pattern:
    def __init__(self):
        pass

    def increment(self, rows):
        
        for i in range(rows):
            stars = "*" * (i + 1)
            print(stars)

    def decrement(self, rows):
        for i in range(rows, 0, -1):
            stars = "*" * (i)
            print(stars)

    def inverseTriangle(self, rows):
        for i in range(rows, 0, -1):
            spaces = ' ' * (rows - i)
            stars = '*' * (2 * i - 1)
            print(spaces + stars + spaces)


    def Triangle(self, rows):
        for i in range(1, rows + 1):
            spaces = ' ' * (rows - i)
            stars = "*" * (2 * i - 1)
            print(spaces + stars + spaces)

    def diamond(self, rows):
        self.Triangle(rows)
        self.inverseTriangle(rows)

    def sandclock(self, rows):
        self.inverseTriangle(rows)
        self.Triangle(rows)

create = Pattern()
create.decrement(5)
create.increment(5)



# # *****
# #  ***
# #   *
# rows = 3

# for i in range(rows , 0, -1):
#     spaces = " " * (rows - i)
#     stars = '*' * (2 * i - 1)
#     print(spaces + stars + spaces)




# #   *  
# #  ***
# # *****
# rows = 3  # Number of rows

# for i in range(1, rows + 1):
#     spaces = ' ' * (rows - i)  # Leading dashes
#     stars = '*' * (2 * i - 1)  # Stars for the current row
#     print(spaces + stars + spaces)  # Construct and print the row




# *
# **
# ***
# n = 5
# for i in range(n):
#     for j in range(n - i - 1, n):
#         print("*", end="")
#     print("")
    
# n = 5
# for i in range(5):
#     stars = "*" * i
#     print(stars)



#git status
#git add . or specific file
#git commit -m "xyz"
#git push origin main