with open('cold\puzz13.txt', 'r') as file:
    content = file.read().split("\n")

sum_result = 0
i = 0
gears = 0

symbols = ['*', '=', '%', '&', '@', '#', '$', '-', '+', '/']

def num_value(i, x):
    num = ''
    while x < len(content[i]) and '0' <= content[i][x] <= '9':
        num += content[i][x]
        x += 1
    return int(num)

def search(i, x):
    while '0' <= content[i][x-1] <= '9' and x > 0:
        x -= 1
    return num_value(i, x)

while i < len(content) and content[i] != '':
    for x in range(len(content[i])):
        adj = 0

        if content[i][x] == '*':
            if '0' <= content[i][x-1] <= '9':
                adj = search(i, x-1)
            if '0' <= content[i][x+1] <= '9':
                if adj != 0:
                    sum_result += adj * search(i, x+1)
                    continue
                adj = search(i, x+1)
            if '0' <= content[i-1][x] <= '9':
                if adj != 0:
                    sum_result += adj * search(i-1, x)
                    continue
                adj = search(i-1, x)
            else:
                if '0' <= content[i-1][x-1] <= '9':
                    if adj != 0:
                        sum_result += adj * search(i-1, x-1)
                        continue
                    adj = search(i-1, x-1)
                if '0' <= content[i-1][x+1] <= '9':
                    if adj != 0:
                        sum_result += adj * search(i-1, x+1)
                        continue
                    adj = search(i-1, x+1)
            if '0' <= content[i+1][x] <= '9':
                if adj != 0:
                    sum_result += adj * search(i+1, x)
                    continue
                adj = search(i+1, x)
            else:
                if '0' <= content[i+1][x-1] <= '9':
                    if adj != 0:
                        sum_result += adj * search(i+1, x-1)
                        continue
                    adj = search(i+1, x-1)
                if '0' <= content[i+1][x+1] <= '9':
                    if adj != 0:
                        sum_result += adj * search(i+1, x+1)
                        continue
                    adj = search(i+1, x+1)

    i += 1

print(sum_result)