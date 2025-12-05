from collections import defaultdict

def read_input(input_file_dir: str) -> list[list[int]]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()
    
    res: list[list[int]] = []

    for line in lines:
        temp_line = []
        for char in line:
            if char == "@":
                temp_line.append(1)
            else:
                temp_line.append(0)
        res.append(temp_line)
    
    return res


def calc_accessible(grid: list[list[int]]) -> int:
    hmap: dict[tuple[int, int], int] = defaultdict(int)

    for r, line in enumerate(grid):
        for c, _ in enumerate(line):
            hmap[(r,c+1)] += grid[r][c]
            hmap[(r,c-1)] += grid[r][c]
            
            hmap[(r-1,c+1)] += grid[r][c]
            hmap[(r-1,c)] += grid[r][c]
            hmap[(r-1,c-1)] += grid[r][c]

            hmap[(r+1,c+1)] += grid[r][c]
            hmap[(r+1,c)] += grid[r][c]
            hmap[(r+1,c-1)] += grid[r][c]

    res = 0

    for r, line in enumerate(grid):
        for c, _ in enumerate(line):
            if grid[r][c] == 1 and hmap[(r,c)] < 4:
                res += 1

    return res


def calc_removeable(grid: list[list[int]]) -> int:
    hmap: dict[tuple[int, int], int] = defaultdict(int)

    for r, line in enumerate(grid):
        for c, _ in enumerate(line):
            hmap[(r,c+1)] += grid[r][c]
            hmap[(r,c-1)] += grid[r][c]
            
            hmap[(r-1,c+1)] += grid[r][c]
            hmap[(r-1,c)] += grid[r][c]
            hmap[(r-1,c-1)] += grid[r][c]

            hmap[(r+1,c+1)] += grid[r][c]
            hmap[(r+1,c)] += grid[r][c]
            hmap[(r+1,c-1)] += grid[r][c]

    res = 0

    while True:
        removed: list[tuple[int, int]] = []

        for r, line in enumerate(grid):
            for c, _ in enumerate(line):
                if grid[r][c] == 1 and hmap[(r,c)] < 4:
                    removed.append((r,c))

        if removed == []:
            break

        for point in removed:
            r, c = point
            res += 1

            grid[r][c] = 0
            hmap[(r,c+1)] -= 1
            hmap[(r,c-1)] -= 1
            
            hmap[(r-1,c+1)] -= 1
            hmap[(r-1,c)] -= 1
            hmap[(r-1,c-1)] -= 1

            hmap[(r+1,c+1)] -= 1
            hmap[(r+1,c)] -= 1
            hmap[(r+1,c-1)] -= 1

    return res


if __name__ == "__main__":
    input_file_dir = "input.txt"
    grid = read_input(input_file_dir)
    print(calc_accessible(grid))
    print(calc_removeable(grid))