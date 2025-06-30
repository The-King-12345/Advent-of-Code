def read_input(input_file_dir: str) -> list[str]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()

    return lines

def calc_price_perm(lines: list[str]) -> int:
    res = 0
    used: set[tuple[int,int]] = set()

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if (row,col) in used:
                continue

            region: set[tuple[int,int]] = set()
            get_region(region, lines, row, col, char)
            used.update(region)

            area = len(region)
            perm = find_perm(region)

            res += area * perm

    return res
    
def get_region(region: set[tuple[int,int]], lines: list[str], row: int, col: int, char: str) -> None:
    if (row,col) in region:
        return 
    region.add((row,col))

    if row - 1 >= 0 and lines[row-1][col] == char:
        get_region(region, lines, row-1, col, char)
    if row + 1 < len(lines) and lines[row+1][col] == char:
        get_region(region, lines, row+1, col, char)
    if col - 1 >= 0 and lines[row][col-1] == char:
        get_region(region, lines, row, col-1, char)
    if col + 1 < len(lines[row]) and lines[row][col+1] == char:
        get_region(region, lines, row, col+1, char)

    return

def find_perm(region: set[tuple[int,int]]) -> int:
    perm = 0
    
    for row,col in region:
        if (row-1,col) not in region:
            perm += 1
        if (row+1,col) not in region:
            perm += 1
        if (row,col+1) not in region:
            perm += 1
        if (row,col-1) not in region:
            perm += 1

    return perm

def calc_price_sides(lines: list[str]) -> int:
    res = 0
    used: set[tuple[int,int]] = set()

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if (row,col) in used:
                continue

            region: set[tuple[int,int]] = set()
            get_region(region, lines, row, col, char)
            used.update(region)

            area = len(region)
            sides = find_sides(region)

            res += area * sides

    return res

def find_sides(region: set[tuple[int,int]]) -> int:
    up: set[tuple[int,int]] = set()
    down: set[tuple[int,int]] = set()
    left: set[tuple[int,int]] = set()
    right: set[tuple[int,int]] = set()

    for row, col in region:
        if (row-1,col) not in region:
            up.add((row,col))
        if (row+1,col) not in region:
            down.add((row,col))
        if (row,col-1) not in region:
            left.add((row,col))
        if (row,col+1) not in region:
            right.add((row,col))

    corners = 0
    for (row, col) in up:
        if (row, col) in left:
            corners += 1
        if (row, col) in right:
            corners += 1
        if (row-1, col-1) in right and (row,col) not in left:
            corners += 1
        if (row-1, col+1) in left and (row,col) not in right:
            corners += 1

    for (row, col) in down:
        if (row, col) in left:
            corners += 1
        if (row, col) in right:
            corners += 1
        if (row+1, col-1) in right and (row,col) not in left:
            corners += 1
        if (row+1, col+1) in left and (row,col) not in right:
            corners += 1
        
    return corners

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(calc_price_perm(lines))
    print(calc_price_sides(lines))