def read_input(input_file_dir: str) -> list[str]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()
    
    return lines

def calc_distinct_pos(lines: list[str]) -> int:
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "^":
                visited: set[tuple[int,int]] = simulate_steps(lines, row, col, 0, -1)

    return len(visited)

def simulate_steps(lines: list[str], row: int, col: int, dx: int, dy: int) -> set[tuple[int,int]]:
    visited: set[tuple[int,int]] = set()
    
    while True:
        visited.add((row,col))
        new_row = row + dy
        new_col = col + dx

        if new_row < 0 or new_col < 0 or new_row >= len(lines) or new_col >= len(lines[row]):
            return visited
        elif lines[new_row][new_col] == "#":
            dx, dy = -dy, dx
        else:
            row = new_row
            col = new_col

def calc_loops(lines: list[str]) -> int:
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "^":
                return simulate_blocks(lines, row, col, 0, -1)
    return 0

def simulate_blocks(lines: list[str], start_row: int, start_col: int, dx: int, dy: int) -> int:
    sum = 0
    
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char != ".":
                continue
            else:
                sum += is_loop(lines, start_row, start_col, dx, dy, (row, col))

    return sum

def is_loop(lines: list[str], row: int, col: int, dx: int, dy: int, block: tuple[int,int]) -> int:
    visited: set[tuple[int,int,int,int]] = set()

    while True:
        if (row, col, dx, dy) in visited:
            return 1

        visited.add((row, col, dx, dy))
        new_row = row + dy
        new_col = col + dx

        if new_row < 0 or new_col < 0 or new_row >= len(lines) or new_col >= len(lines[row]):
            return 0
        elif lines[new_row][new_col] == "#" or (new_row == block[0] and new_col == block[1]):
            dx, dy = -dy, dx
        else:
            row = new_row
            col = new_col

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(calc_distinct_pos(lines))
    print(calc_loops(lines))


