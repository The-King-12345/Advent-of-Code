def read_input(input_file_dir: str) -> tuple[list[tuple[int, int,]], list[int]]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()
    
    ranges: list[tuple[int, int]] = []
    ids: list[int] = []

    for line in lines:
        if "-" in line:
            first, second = line.split("-")
            ranges.append((int(first), int(second)))
        elif line != "":
            ids.append(int(line))
        
    return ranges, ids


def calc_fresh(ranges: list[tuple[int, int]], ids: list[int]) -> int:  
    res = 0

    for id in ids:
        if is_fresh(ranges, id):
            res += 1

    return res


def is_fresh(ranges: list[tuple[int,int]], id: int) -> bool:
    for rng in ranges:
        first, last = rng
        if id >= first and id <= last:
            return True
    return False


def count_fresh(ranges: list[tuple[int, int]]) -> int:
    sr = sorted(ranges)

    partitions: list[tuple[int, int]] = []
    
    curr = 0
    while curr < len(sr):
        partition = (sr[curr][0], sr[curr][1])

        next = curr + 1

        while next < len(sr) and sr[next][0] >= partition[0] and sr[next][0] <= partition[1]:
            if sr[next][1] > partition[1]:
                partition = (partition[0], sr[next][1])

            next += 1

        partitions.append(partition)

        curr = next

    res = 0

    for partition in partitions:
        res += (partition[1]-partition[0]+1)

    return res


if __name__ == "__main__":
    input_file_dir = "input.txt"
    ranges, ids = read_input(input_file_dir)
    print(calc_fresh(ranges, ids))
    print(count_fresh(ranges))