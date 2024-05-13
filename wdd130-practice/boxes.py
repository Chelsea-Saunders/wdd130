""" A manufacturing company needs a program that will help its employees pack 
manufactured items into boxes for shipping. Write a Python program named 
boxes.py that asks the user for two integers:

-the number of manufactured items
-the number of items that the user will pack per box
-Your program must compute and print the number of boxes necessary to hold 
the items. This must be a whole number. Note that the last box may be 
packed with fewer items than the other boxes."""

# import math module
import math

# get numbers from user
items = int(input("What is the total number of manufactured items:  "))
items_per_box = int(input("How many items will fit in each box:  "))

# compute the number ofneeded boxex (dividing and calling math.ceil)
total = math.ceil (items / items_per_box)

# blank line
print()
# show mathmatical results
print (f"You will need {total} boxes.")
# another way to write it:
# print (f"To fit {items_per_box} of the {items} per box, you'll need"
#   f" {total} boxes.)