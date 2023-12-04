import re 

with open('cold\puzzl3.txt', 'r') as file:
    content = file.read().split('\n')

    print(content)


def calculate_color_product_sum():
    sum = 0
    i = 0

    while i < len(content) and content[i] != '':
        counter = {'red': 0, 'blue': 0, 'green': 0}
        str = content[i][content[i].index(': ') + 2:]
        word = re.findall(r'\w+', str)

        for j in range(1, len(word), 2):
            if int(word[j - 1]) > counter[word[j]]:
                counter[word[j]] = int(word[j - 1])

        sum += counter['red'] * counter['blue'] * counter['green']

        i += 1

    return sum

print(calculate_color_product_sum())