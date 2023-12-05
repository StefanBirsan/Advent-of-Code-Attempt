import re
from typing import List

class Range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

class MapEntry:
    def __init__(self, src: Range, dst: Range):
        self.src = src
        self.dst = dst

class Map:
    def __init__(self, entries: List[MapEntry]):
        self.entries = entries

class Solution:
    def part_two(self, input_path: str) -> int:
        with open(input_path, 'r') as file:
            input_str = file.read()
        return self.solve(input_str, lambda ints: [Range(v[0], v[0] + v[1] - 1) for v in zip(*[iter(ints)] * 2)])

    def solve(self, input_str: str, parse_ranges) -> int:
        blocks = input_str.split("\n\n")
        ranges = list(parse_ranges(self.parse_ints(blocks[0])))
        maps = [self.parse_map(block) for block in blocks[1:]]

        ranges = self.lookup(ranges, maps)

        return min(r.start for r in ranges)

    def parse_ints(self, input_str: str) -> List[int]:
        return [int(m.group()) for m in re.finditer(r'\d+', input_str)]

    def parse_map(self, input_str: str) -> Map:
        return Map([self.parse_map_entry(line) for line in input_str.split("\n")[1:]])

    def parse_map_entry(self, line: str) -> MapEntry:
        parts = [int(part) for part in line.split(" ")]
        src = Range(parts[1], parts[2] + parts[1] - 1)
        dst = Range(parts[0], parts[2] + parts[0] - 1)
        return MapEntry(src, dst)

    def lookup(self, ranges: List[Range], maps: List[Map]) -> List[Range]:
        for m in maps:
            ranges = [r for range_ in ranges for r in self.lookup_range(range_, m)]
            ranges = self.pack(ranges)
        return ranges

    def pack(self, ranges: List[Range]) -> List[Range]:
        ranges = sorted(ranges, key=lambda x: x.start)
        res = []
        range_ = ranges[0]
        for i in range(1, len(ranges)):
            if range_.end == ranges[i].start - 1:
                range_ = Range(range_.start, ranges[i].end)
            else:
                res.append(range_)
                range_ = ranges[i]
        res.append(range_)
        return res

    def lookup_range(self, range_: Range, map_: Map) -> List[Range]:
        q = [range_]
        result = []
        while q:
            range_ = q.pop(0)
            found = False
            for entry in map_.entries:
                if entry.src.start <= range_.start and range_.end <= entry.src.end:
                    shift = entry.dst.start - entry.src.start
                    result.append(Range(range_.start + shift, range_.end + shift))
                    found = True
                elif range_.start < entry.src.start and entry.src.start <= range_.end:
                    q.extend([Range(range_.start, entry.src.start - 1), Range(entry.src.start, range_.end)])
                    found = True
                elif range_.start < entry.src.end and entry.src.end <= range_.end:
                    q.extend([Range(range_.start, entry.src.end), Range(entry.src.end + 1, range_.end)])
                    found = True
            if not found:
                result.append(Range(range_.start, range_.end))
        return result

solver = Solution()
input_file_path = "cold\map.txt"
print(solver.part_two(input_file_path))
