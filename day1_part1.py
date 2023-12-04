import re

calibration_values = []
puzzle_path = "cold/puzzle.txt"  # Adjust the path to your file

def extract_calibration_values(line):
    # Extract the first and last digits and combine them into a two-digit number
    first_digit = re.search(r'\d', line).group()
    last_digit = re.search(r'\d', line[::-1]).group()
    calibration_value = int(first_digit + last_digit)
    return calibration_value

# Open the file, read its content, and extract calibration values
with open(puzzle_path, 'r') as file:
    for line in file:
        calibration_value = extract_calibration_values(line)
        calibration_values.append(calibration_value)

# Calculate the sum of calibration values
sum_of_calibration_values = sum(calibration_values)
print("Sum of calibration values:", sum_of_calibration_values)
