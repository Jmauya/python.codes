# bmi.py

# Input your mass (in kilograms) and height (in meters)
mass = 70       # Example: 70 kg
height = 1.75   # Example: 1.75 meters

# Formula: BMI = mass / height squared
bmi = mass / (height ** 2)

# Printing the result
print(f"Mass: {mass} kg")
print(f"Height: {height} m")
print(f"Calculated BMI: {bmi:.2f}")

# Author's Note: Remember, this doesn't account for muscle mass, bone density, or overall composition
