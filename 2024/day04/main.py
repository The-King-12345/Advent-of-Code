def read_input(input_file_dir: str) -> list[str]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()
    return lines

def calc_xmas(lines: list[str]):
    target = "XMAS"
    sum = 0
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "X":
                sum += check_line(lines, target, row, col, 0, 1)
                sum += check_line(lines, target, row, col, 0, -1)
                sum += check_line(lines, target, row, col, 1, 0)
                sum += check_line(lines, target, row, col, -1, 0)
                sum += check_line(lines, target, row, col, 1, 1)
                sum += check_line(lines, target, row, col, -1, 1)
                sum += check_line(lines, target, row, col, -1, -1)
                sum += check_line(lines, target, row, col, 1, -1)
    return sum

def check_line(lines: list[str], target: str, row: int, col: int, rowstep: int, colstep: int) -> int:
    for i, letter in enumerate(target):
        new_row = row + i * rowstep
        new_col = col + i * colstep

        if new_row < 0 or new_col < 0 or new_row >= len(lines) or new_col >= len(lines[row]):
            return 0
        if lines[new_row][new_col] != letter:
            return 0
    return 1

def calc_mas(lines: list[str]):
    target = "MAS"
    sum = 0
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "A" and check_cross(lines, target, row, col):
                sum += 1
    return sum

def check_cross(lines: list[str], target: str, row: int, col: int) -> bool:
    if check_line(lines, target, row-1, col-1, 1, 1) or check_line(lines, target, row+1, col+1, -1, -1):
        if check_line(lines, target, row-1, col+1, 1, -1) or check_line(lines, target, row+1, col-1, -1, 1):
            return True
    
    return False

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(calc_xmas(lines))
    print(calc_mas(lines))