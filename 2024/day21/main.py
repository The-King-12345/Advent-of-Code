from itertools import product
from collections import deque
from functools import cache

def read_input(input_file_dir: str) -> list[str]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()

    return lines

def find_path(start: tuple[int,int], end: tuple[int,int], keypad: list[tuple[int, int]]) -> list[str]:
    if start == end:
        return ["A"]
    queue: deque[tuple[int,int,str]] = deque([(*start, "")])
    best_length = 100
    optimal_paths: list[str] = []
    while queue:
        row, col, path = queue.popleft()
        for nr, nc, move in [(row-1,col,"^"),(row+1,col,"v"),(row,col-1,"<"),(row,col+1,">")]:
            if (nr, nc) not in keypad: 
                continue
            if (nr, nc) == end and len(path) + 1 > best_length: 
                return optimal_paths
            if (nr, nc) == end:
                optimal_paths.append(path + move + "A")
                best_length = min(len(path) + 2, best_length)
            else:
                queue.append((nr,nc,path+move))
    
    return optimal_paths

def calc_complexity(codes: list[str], depth: int) -> int:
    res = 0

    for code in codes:
        paths: list[list[str]] = []
        best_length = float("inf")

        for key1, key2 in zip("A" + code, code):
            paths += [num_pad_paths[(num_keys[key1],num_keys[key2])]]
        for segment in product(*paths):
            best_length = min(best_length, find_min_length("".join(segment), depth))

        res += int(best_length) * int(code[:-1])

    return res

@ cache
def find_min_length(code: str, depth: int) -> int:
    if depth == 0:
        return len(code)
    
    res = 0
    for key1, key2 in zip("A" + code, code):
        res += min(find_min_length(seq, depth - 1) for seq in dir_pad_paths[(dir_keys[key1],dir_keys[key2])])

    return res

if __name__ == "__main__":
    input_file_dir = "input.txt"
    codes = read_input(input_file_dir)

    num_keys: dict[str, tuple[int, int]] = {
        "7": (0,0),
        "8": (0,1),
        "9": (0,2),
        "4": (1,0),
        "5": (1,1),
        "6": (1,2),
        "1": (2,0),
        "2": (2,1),
        "3": (2,2),
        "0": (3,1),
        "A": (3,2)
    }

    dir_keys: dict[str, tuple[int, int]] = {
        "^": (0,1),
        "A": (0,2),
        "<": (1,0),
        "v": (1,1),
        ">": (1,2)
    }

    num_pad_paths: dict[tuple[tuple[int, int], tuple[int, int]], list[str]] = {
        (start, end): find_path(start, end, list(num_keys.values())) 
        for start in num_keys.values() 
        for end in num_keys.values()
    }
    
    dir_pad_paths: dict[tuple[tuple[int, int], tuple[int, int]], list[str]] = {
        (start, end): find_path(start, end, list(dir_keys.values())) 
        for start in dir_keys.values() 
        for end in dir_keys.values()
    }

    print(calc_complexity(codes, 2))
    print(calc_complexity(codes, 25))
