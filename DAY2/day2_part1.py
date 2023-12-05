import re 

with open('cold\puzzl3.txt', 'r') as file:
    content = file.read().split('\n')

    print(content)


def calculate_limit_exceed_sum():
    sum = 0
    i = 0
    limit = {'red': 12, 'blue': 14, 'green': 13}

    while i <len(content) and content[i] != '':
        exceed = False
        str = content[i][content[i].index(': ') + 2:]
        word = re.findall(r'\w+', str)

        for j in range(1, len(word), 2):
            if int(word[j - 1]) > limit[word[j]]:
                exceed = True
                break

        if not exceed:
            sum += i + 1

        i += 1

    return sum



print(calculate_limit_exceed_sum())
    