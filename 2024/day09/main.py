def read_input(input_file_dir: str) -> list[int]:
    with open(input_file_dir) as f:
        line = f.read()

    digits = [int(n) for n in line]

    return digits

def calc_checksum(line: list[int]) -> int:
    filesystem: list[int] = make_filesystem(line)
    condensed: list[int] = condense_filesystem(filesystem)
    return checksum(condensed)

def make_filesystem(line: list[int]) -> list[int]:
    filesystem: list[int] = []
    
    for i in range(0,len(line),2):
        digit = i // 2
        freq = line[i]
        if i + 1 < len(line):
            space = line[i+1]
        else:
            space = 0

        for _ in range(freq):
            filesystem.append(digit)
        for _ in range(space):
            filesystem.append(-1)

    return filesystem

def condense_filesystem(filesystem: list[int]) -> list[int]:
    condensed: list[int] = []
    last_pointer = len(filesystem) - 1

    for i, num in enumerate(filesystem):
        if i > last_pointer:
            return condensed

        if num == -1:
            while filesystem[last_pointer] == -1:
                last_pointer -= 1
                if i > last_pointer:
                    return condensed
            
            condensed.append(filesystem[last_pointer])
            last_pointer -= 1
        else:
            condensed.append(num)

    return condensed

def checksum(condensed: list[int]) -> int:
    res = 0
    for i, num in enumerate(condensed):
        if num != -1:
            res += i * int(num)
    return res

def calc_compacted_checksum(line: list[int]) -> int:
    filesystem: list[int] = make_filesystem(line)
    compacted: list[int] = compact_filesystem(filesystem, line)
    return checksum(compacted)

def compact_filesystem(filesystem: list[int], line: list[int]) -> list[int]:
    condensed: list[int] = list(filesystem)

    for i in range((len(line)-1)//2,-1,-1):
        block_loc, size = count_size(condensed, i)
        space_loc = find_space(condensed, size)

        if space_loc >= 0 and space_loc < block_loc:
            for j in range(size):
                pos1 = space_loc + j
                pos2 = block_loc + j

                condensed[pos1] = condensed[pos2]
                condensed[pos2] = -1

    return condensed

def count_size(filesystem: list[int], id: int) -> tuple[int,int]:
    res = 0
    target = id
    found = False

    for i, num in enumerate(reversed(filesystem)):
        if not found:
            if num == target:
                found = True
                res += 1
        else:
            if num == target:
                res += 1
            else:
                return len(filesystem)-i, res

    return 0, res

def find_space(filesystem: list[int], size: int) -> int:
    run_start = 0
    run = 0
    running = False

    for i, num in enumerate(filesystem):
        if num == -1:
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
    print(calc_checksum(line))
    print(calc_compacted_checksum(line))