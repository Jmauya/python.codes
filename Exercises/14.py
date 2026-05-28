# hypotenuse.py
import math

print(" Hypotenuse Calculator ")
print("--------------------------")

# Ask the user for the lengths of the two shorter sides
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

# Pythagorean Theorem formula: c = sqrt(a^2 + b^2)
c = math.sqrt((a ** 2) + (b ** 2))

# Print the result rounded to two decimal places
print(f"\nThe length of the hypotenuse c is: {c:.2f} 🎉")
