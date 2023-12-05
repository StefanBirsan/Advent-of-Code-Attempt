with open('cold\puzz13.txt', 'r') as file:
    content = file.read().split("\n")

sum_result = 0
i = 0

symbols = ['*', '=', '%', '&', '@', '#', '$', '-', '+', '/']

def num_value(i, x):
    num = ''
    while x < len(content[i]) and '0' <= content[i][x] <= '9':
        num += content[i][x]
        x += 1
    return int(num)

def search(i, x):
    while x > 0 and '0' <= content[i][x-1] <= '9':
        x -= 1
    return num_value(i, x)

def is_symbol(char):
    return char in symbols

while i < len(content):
    x = 0
    while x < len(content[i]):
        adj = 0

        if is_symbol(content[i][x]):
            if x > 0 and '0' <= content[i][x-1] <= '9':
                adj = search(i, x-1)
                sum_result += adj
            if x + 1 < len(content[i]) and '0' <= content[i][x+1] <= '9':
                adj = search(i, x+1)
                sum_result += adj
            if i > 0 and '0' <= content[i-1][x] <= '9':
                adj = search(i-1, x)
                sum_result += adj
            else:
                if i > 0 and x > 0 and '0' <= content[i-1][x-1] <= '9':
                    adj = search(i-1, x-1)
                    sum_result += adj
                if i > 0 and x + 1 < len(content[i-1]) and '0' <= content[i-1][x+1] <= '9':
                    adj = search(i-1, x+1)
                    sum_result += adj
            if i + 1 < len(content) and '0' <= content[i+1][x] <= '9':
                adj = search(i+1, x)
                sum_result += adj
            else:
                if i + 1 < len(content) and x > 0 and '0' <= content[i+1][x-1] <= '9':
                    adj = search(i+1, x-1)
                    sum_result += adj
                if i + 1 < len(content) and x + 1 < len(content[i+1]) and '0' <= content[i+1][x+1] <= '9':
                    adj = search(i+1, x+1)
                    sum_result += adj
        x += 1
    i += 1

print(sum_result)