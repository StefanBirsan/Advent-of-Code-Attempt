import math
import re

with open('DAY6\input.txt', 'r') as file:
    input_data = file.read()

class Solution:
    def PartOne(self, input):
        return self.Solve(input)

    def PartTwo(self, input):
        return self.Solve(input.replace(" ", ""))

    def Solve(self, input):
        rows = input.split("\n")
        times = self.Parse(rows[0])
        records = self.Parse(rows[1])

        res = 1
        for i in range(len(times)):
            res *= self.WinningMoves(times[i], records[i])

        return res

    def WinningMoves(self, time, record):
        # If we wait x ms, our boat moves `(time - x) * x` millimeters.
        # This breaks the record when `(time - x) * x > record`
        # or `-x^2  + time * x - record > 0`.

        # get the roots first
        x1, x2 = self.SolveEq(-1, time, -record)

        # integers in between the roots
        maxX = math.ceil(x2) - 1
        minX = math.floor(x1) + 1
        return maxX - minX + 1

    # solves ax^2 + bx + c = 0 (supposing two different roots)
    def SolveEq(self, a, b, c):
        d = math.sqrt(b * b - 4 * a * c)
        x1 = (-b - d) / (2 * a)
        x2 = (-b + d) / (2 * a)
        return min(x1, x2), max(x1, x2)

    def Parse(self, input):
        return [int(m.group()) for m in re.finditer(r'\d+', input)]
    
    

solution = Solution()
result_part_one = solution.PartOne(input_data)
result_part_two = solution.PartTwo(input_data)

print(f"Part One Result: {result_part_one}")
print(f"Part Two Result: {result_part_two}")
