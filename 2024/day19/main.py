from functools import cache

def read_input(input_file_dir: str) -> tuple[list[str], list[str]]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()

    patterns: list[str] = []
    designs: list[str] = []

    for i, line in enumerate(lines):
        if i == 0:
            for pattern in line.split(", "):
                patterns.append(pattern)
        elif i > 1:
            designs.append(line)

    return patterns, designs

def calc_possible_designs(patterns: list[str], designs: list[str]) -> int:
    res = 0

    for design in designs:
        if is_possible(patterns, design):
            res += 1
            
    return res

def is_possible(patterns: list[str], design: str) -> bool:
    if design in patterns:
        return True
    
    for pattern in patterns:
        if design.startswith(pattern):
            if is_possible(patterns, design[len(pattern):]):
                return True
    return False

def calc_arrangements(patterns: list[str], designs: list[str]) -> int:
    res = 0

    for design in designs:
        res += get_arrangements(tuple(patterns), design)

    return res

@cache
def get_arrangements(patterns: tuple[str], design: str) -> int:
    if design == "":
        return 1
    
    res = 0
    for pattern in patterns:
        if design.startswith(pattern):
            res += get_arrangements(tuple(patterns), design[len(pattern):])
    return res

if __name__ == "__main__":
    input_file_dir = "input.txt"
    patterns, designs = read_input(input_file_dir)
    print(calc_possible_designs(patterns, designs))
    print(calc_arrangements(patterns, designs))
