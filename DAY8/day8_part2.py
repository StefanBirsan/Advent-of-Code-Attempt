import re
import math

with open('DAY8\input.txt', 'r') as file:
    input = [line.strip() for line in file]

# code for both parts actually :D
instructions = input[0]

nodes = {}
for line in input[2:]:
    # use regex to match node, left and right
    node, left, right = re.findall(r"\b\w{3}\b", line)
    nodes[node] = (left, right)

def calculate_steps(curr_node, goal_nodes):
    step_idx = 0
    num_steps = 0
    
    # go through nodes starting at curr_node until goal_node is reached and count number of steps
    while curr_node not in goal_nodes:

        left, right = nodes[curr_node]
        
        if instructions[step_idx] == 'L':
            curr_node = left
    
        elif instructions[step_idx] == 'R':
            curr_node = right
        
        # increment step counter
        num_steps += 1
        
        if (step_idx + 1) == len(instructions):
            step_idx = 0
        else:
            step_idx += 1
    
    return num_steps

# part 1
# go through nodes starting at AAA until ZZZ is reached and count number of steps
result_part_1 = calculate_steps('AAA', ['ZZZ'])

# part 2
# find all start and end nodes
start_nodes = [node for node in nodes.keys() if re.match(r"\w{2}A", node)]
end_nodes = [node for node in nodes.keys() if re.match(r"\w{2}Z", node)]

# find steps to end node for every node = end of first cycle
steps = [calculate_steps(node, end_nodes) for node in start_nodes]

# find least common multiple of the number of steps until end node of every node
result_part_2 =  math.lcm(*steps)

print(f"Part 1: {result_part_1}") 
print(f"Part 2: {result_part_2}") 