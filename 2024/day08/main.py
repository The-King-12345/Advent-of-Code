from itertools import combinations

def read_input(input_file_dir: str) -> list[str]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()
    return lines

def make_antenas(lines: list[str]) -> dict[str, list[tuple[int,int]]]:
    antennas: dict[str, list[tuple[int,int]]] = {}
    
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char != ".":
                if char not in antennas:
                    antennas[char] = [(row,col)]
                else:
                    antennas[char] += [(row,col)]

    return antennas

def calc_antinodes(lines: list[str]) -> int:
    antennas: dict[str, list[tuple[int,int]]] = make_antenas(lines)
    antinodes: set[tuple[int,int]] = set()

    for positions in antennas.values():
        add_antinodes(antinodes, positions, lines)

    return len(antinodes)
            
def add_antinodes(antinodes: set[tuple[int,int]], positions: list[tuple[int,int]], lines: list[str]) -> None:
    pairs: list[tuple[tuple[int,int], tuple[int,int]]] = list(combinations(positions,2))

    for pos1, pos2 in pairs:
        row1, col1 = pos1 
        row2, col2 = pos2 

        if row1 > row2:
            new_row1 = row1 + abs(row1-row2)
            new_row2 = row2 - abs(row1-row2)
        else:
            new_row1 = row1 - abs(row1-row2)
            new_row2 = row2 + abs(row1-row2)

        if col1 > col2:
            new_col1 = col1 + abs(col1-col2)
            new_col2 = col2 - abs(col1-col2)
        else:
            new_col1 = col1 - abs(col1-col2)
            new_col2 = col2 + abs(col1-col2)

        if in_bounds(lines, new_row1, new_col1):
            antinodes.add((new_row1,new_col1))
        if in_bounds(lines, new_row2, new_col2):
            antinodes.add((new_row2,new_col2))

    return

def in_bounds(lines, row, col) -> bool:
    return row >= 0 and col >= 0 and row < len(lines) and col < len(lines[row])

def calc_resonant_antinodes(lines: list[str]) -> int:
    antennas: dict[str, list[tuple[int,int]]] = make_antenas(lines)
    antinodes: set[tuple[int,int]] = set()

    for positions in antennas.values():
        add_resonant_antinodes(antinodes, positions, lines)

    return len(antinodes)

def add_resonant_antinodes(antinodes: set[tuple[int,int]], positions: list[tuple[int,int]], lines: list[str]) -> None:
    pairs: list[tuple[tuple[int,int], tuple[int,int]]] = list(combinations(positions,2))

    for pos1, pos2 in pairs:
        row1, col1 = pos1 
        row2, col2 = pos2 
        dx = col2-col1
        dy = row2-row1

        add_line(antinodes, lines, row1, col1, dx, dy)
        add_line(antinodes, lines, row1, col1, -dx, -dy)

    return

def add_line(antinodes: set[tuple[int,int]], lines: list[str], row: int, col: int, dx: int, dy: int) -> None:
    while in_bounds(lines, row,col):
        antinodes.add((row,col))

        row += dy
        col += dx
        
    return 

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(calc_antinodes(lines))
    print(calc_resonant_antinodes(lines))

