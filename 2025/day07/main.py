import sys
from functools import cache

def read_input(input_file_dir: str) -> list[list[int]]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()
    
    graph: list[list[int]] = []

    for line in lines:
        row = []

        for char in line:
            if char == ".":
                row.append(0)
            else:
                row.append(1)

        if 1 in row:
            graph.append(row)

    return graph


def calc_splits(graph: list[list[int]]) -> int:
    res = 0

    curr = graph[0]

    for row in graph[1:]:
        new_row, splits = split_beam(curr, row)
        curr = new_row
        res += splits

    return res


def split_beam(row1: list[int], row2: list[int]) -> tuple[list[int], int]:
    new_row = [0] * len(row1)
    splits = 0

    for i in range(len(row1)):
        if row1[i] == 1:
            if row2[i] == 0:
                new_row[i] = 1
            elif row2[i] == 1:
                new_row[i+1] = 1
                new_row[i-1] = 1
                splits += 1

    return new_row, splits


def calc_timelines(graph: list[list[int]]) -> int:

    @cache
    def search_timelines(row: int, beam: int) -> int:
        if row == len(graph) - 1:
            if graph[row][beam] == 1:
                return 2
            else:
                return 1
        else:
            if graph[row][beam] == 1:
                return search_timelines(row+1, beam+1) + search_timelines(row+1, beam-1)
            else:
                return search_timelines(row+1, beam)
            

    for i, num in enumerate(graph[0]):
        if num == 1:
            return search_timelines(1, i)
        
    return 0


if __name__ == "__main__":
    input_file_dir = "input.txt"

    if len(sys.argv) > 1:
        input_file_dir = sys.argv[1]

    graph = read_input(input_file_dir)
    print(calc_splits(graph))
    print(calc_timelines(graph))
