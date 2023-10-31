#Task 1
import math
# Input the radius from the user
radius = float(input("Input the radius of the circle: "))

# Calculate the area of the circle
area = math.pi * (radius ** 2)

print(f"The area of the circle with radius {radius} is: {area}")



#Task 2
#input the filename from user
filename = input("Input the Filename: ")

#find the file extension
file_extension = filename.split('.')[-1]

print(f"The extension of the file is: '{file_extension}'")
