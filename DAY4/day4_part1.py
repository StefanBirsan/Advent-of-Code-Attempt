with open('cold\ice.txt', 'r') as file:
    content = file.read().split("\n")

i = 0
one = 0
instances = [1] * len(content)

while i < len(content) and content[i] != '0':
    str_parts = content[i][content[i].index(': ') + 2:].replace("  ", " ").split(" | ")

    counter = sum(1 for item in str_parts[0].split(" ") if item in str_parts[1].split(" "))

    one += 0 if counter == 0 else 2 ** (counter - 1)

    i += 1

print(one)