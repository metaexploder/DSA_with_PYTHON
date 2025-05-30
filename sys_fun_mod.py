import sys

print("Script name:", sys.argv[0])
if len(sys.argv) > 1:
    print("User passed:", sys.argv[1])
else:
    print("No argument passed.")
