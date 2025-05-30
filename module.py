# import json #Used to work with JSON data — for APIs, config files, etc.
import csv #Used to read/write Excel-like files (.csv)
# import os #Used to interact with your operating system — folders, files, paths
# import math	#Advanced math operations (sqrt, pow, etc.)
# import random	#Generate random numbers/data
# import datetime	#Deal with date/time
# import sys	#Interact with Python runtime, arguments
# import logging	#Create logs instead of print statements
# import time	#Sleep/delay, measure time


# Writing
with open("student_marks.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Math", "Science"])
    data = [
        ["Arjun", 88, 91],
        ["Vishu", 95, 98]
    ]
    writer.writerows(data)

# Reading
with open("student_marks.csv", "r") as f:
    reader = csv.reader(f)
    print(type(reader), type(f), type("hello"), type(45))
