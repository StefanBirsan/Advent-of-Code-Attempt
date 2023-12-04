import re

def first(s):
    for char in s:
        if '1' <= char <= '9':
            return int(char) * 10
    return 0

def last(s):
    for char in reversed(s):
        if '1' <= char <= '9':
            return int(char)
    return 0

def one(lines):
    total_sum = 0
    for line in lines:
        if not line:
            continue
        total_sum += first(line)
        total_sum += last(line)
    return total_sum

def two(lines):
    total_sum = 0
    replacements = {
        'one': 'o1e',
        'two': 't2w',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e'
    }

    for line in lines:
        if not line:
            continue
        for item, replacement in replacements.items():
            line = line.replace(item, replacement)
       
        first_char = first(line)
        if first_char is not None:
            total_sum += first_char
        last_char = last(line)
        if last_char is not None:
            total_sum += last_char
    return total_sum

if __name__ == "__main__":
    with open('cold\puzzle.txt', 'r') as file:
        content = file.read().split("\n")

    result_one = one(content)
    result_two = two(content)

    if result_one is not None:
        print(result_one)
    if result_two is not None:
        print(result_two)

