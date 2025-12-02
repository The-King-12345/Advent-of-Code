def read_input(input_file_dir: str) -> list[tuple[int, int]]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()
    
    res: list[tuple[int, int]] = []

    for line in lines:
        if line[0:1] == "L":
            dir = -1
        else:
            dir = 1

        val = int(line[1:])
        res.append((dir, val))
    
    return res


def calc_pass(seq: list[tuple[int, int]], start: int) -> int:
    res = 0
    curr = start

    for rotation in seq:
        dir, val = rotation

        curr = (curr + (val * dir)) % 100

        if curr == 0:
            res += 1

    return res


def calc_new_pass(seq: list[tuple[int, int]], start: int) -> int:
    res = 0
    curr = start

    for rotation in seq:
        dir, val = rotation

        for _ in range(val):
            curr += dir
            if curr % 100 == 0:
                res += 1

    return res
  

if __name__ == "__main__":
    input_file_dir = "input.txt"
    seq = read_input(input_file_dir)
    print(calc_pass(seq, 50))
    print(calc_new_pass(seq, 50))