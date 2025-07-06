from re import findall

def read_input(input_file_dir: str) -> tuple[list[list[int]], list[list[int]]]:
    with open(input_file_dir) as f:
        text = f.read()

    locks: list[list[int]] = []
    keys: list[list[int]] = []

    if matches := findall(r"\#{5}\n(?:(?:[#.]){5}\n){5}\.{5}", text):
        for match in matches:
            locks.append(get_col_heights(match))

    if matches := findall(r"\.{5}\n(?:(?:[#.]){5}\n){5}\#{5}", text):
        for match in matches:
            keys.append(get_col_heights(match))

    return locks, keys

def get_col_heights(text: str) -> list[int]:
    heights: list[int] = [-1] * 5
    lines: list[str] = text.splitlines()
    for line in lines:
        for col, char in enumerate(line):
            heights[col] += 1 if char == "#" else 0
    return heights

def calc_unique_pairs(locks: list[list[int]], keys: list[list[int]]) -> int:
    pairs: set[tuple[int,int]] = set()
    
    for i, lock in enumerate(locks):
        for j, key in enumerate(keys):
            if not pair_valid(lock, key): continue
            pairs.add((i,j))

    return len(pairs)

def pair_valid(lock, key) -> bool:
    for a, b in zip(lock, key):
        if a + b > 5: return False
    return True

if __name__ == "__main__":
    input_file_dir = "input.txt"
    locks, keys = read_input(input_file_dir)
    print(calc_unique_pairs(locks, keys))

    
