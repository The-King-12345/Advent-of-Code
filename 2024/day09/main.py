def read_input(input_file_dir: str) -> list[int]:
    with open(input_file_dir) as f:
        line = f.read()

    digits = [int(n) for n in line]

    return digits

def calc_checksum(line: list[int], type: str) -> int:
    filesystem: list[str] = make_filesystem(line)
    condensed: list[str] = []

    if type == "condense":
        condensed = condense_filesystem(filesystem)
    elif type == "compact": 
        condensed = compact_filesystem(filesystem, line)
    
    return checksum(condensed)

def make_filesystem(line: list[int]) -> list[str]:
    filesystem: list[str] = []
    
    for i in range(0,len(line),2):
        digit = i // 2
        freq = line[i]
        if i + 1 < len(line):
            space = line[i+1]
        else:
            space = 0

        for _ in range(freq):
            filesystem.append(str(digit))
        for _ in range(space):
            filesystem.append(".")

    return filesystem

def condense_filesystem(filesystem: list[str]) -> list[str]:
    condensed: list[str] = []
    last_pointer = len(filesystem) - 1

    for i, char in enumerate(filesystem):
        if i > last_pointer:
            return condensed

        if char == ".":
            while filesystem[last_pointer] == ".":
                last_pointer -= 1
                if i > last_pointer:
                    return condensed
            
            condensed.append(filesystem[last_pointer])
            last_pointer -= 1
        else:
            condensed.append(char)

    return condensed

def checksum(condensed: list[str]) -> int:
    res = 0
    for i, char in enumerate(condensed):
        if char != ".":
            res += i * int(char)
    return res

def compact_filesystem(filesystem: list[str], line: list[int]) -> list[str]:
    condensed: list[str] = list(filesystem)

    for i in range((len(line)-1)//2,-1,-1):
        block_loc, size = count_size(condensed, i)
        space_loc = find_space(condensed, size, block_loc)

        if space_loc >= 0:
            for j in range(size):
                pos1 = space_loc + j
                pos2 = block_loc + j

                condensed[pos1] = condensed[pos2]
                condensed[pos2] = "."

    return condensed

def count_size(filesystem: list[str], id: int) -> tuple[int,int]:
    res = 0
    target = str(id)
    found = False

    for i, char in enumerate(reversed(filesystem)):
        if not found:
            if char == target:
                found = True
                res += 1
        else:
            if char == target:
                res += 1
            else:
                return len(filesystem)-i, res

    return 0, res

def find_space(filesystem: list[str], size: int, stop: int) -> int:
    run_start = 0
    run = 0
    running = False

    for i, char in enumerate(filesystem):
        if i >= stop:
            return -1

        if char == ".":
            if not running:
                run_start = i
                running = True
            run += 1
        else:
            if run >= size:
                return run_start
            running = False
            run = 0

    if run >= size:
        return run_start
    else:
        return -1

if __name__ == "__main__":
    line = read_input("input.txt")
    print(calc_checksum(line, "condense"))
    print(calc_checksum(line, "compact"))



