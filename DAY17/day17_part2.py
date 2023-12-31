from heapq import *

def main() -> None:
    data = open("DAY17\input.txt").read().strip()

    grid = tuple(data.split("\n"))

    width = len(grid[0])
    height = len(grid)

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    heap = [(0, 0, 0, 0, 0), (0, 0, 0, 1, 0)]
    seen = set()

    while len(heap) > 0:
        heat, x, y, direction, streak = heappop(heap)

        if (x, y, direction, streak) in seen:
            continue

        seen.add((x, y, direction, streak))

        if x == width - 1 and y == height - 1:
            if streak > 3:
                print(heat)
                return

        dx, dy = directions[direction]
        x += dx
        y += dy

        if x < 0 or x >= width or y < 0 or y >= height:
            continue

        heat += int(grid[y][x])
        streak += 1

        if streak < 10:
            heappush(heap, (heat, x, y, direction, streak))

        if streak > 3:
            heappush(heap, (heat, x, y, (direction + 1) % 4, 0))
            heappush(heap, (heat, x, y, (direction - 1) % 4, 0))

if __name__ == "__main__":
    main()