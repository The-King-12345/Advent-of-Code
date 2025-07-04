def read_input(input_file_dir: str) -> list[int]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()

    return list(map(int, lines))

def calc_sum(lines: list[int], repetitions: int) -> int:
    res = 0

    for line in lines:
        num = line
        for _ in range(repetitions):
            num = get_next(num)
        res += num

    return res

def get_next(num: int) -> int:
    num = num ^ (num * 64) % 16777216
    num = num ^ (num // 32) % 16777216
    num = num ^ (num * 2048) % 16777216
    return num

def most_bananas(lines: list[int], repetitions: int) -> int:
    buyer_nums: list[list[int]] = []
    for line in lines:
        num = line
        add_list: list[int] = [num % 10]
        for _ in range(repetitions):
            add_list.append(get_next(num) % 10)
            num = get_next(num)
        buyer_nums.append(add_list)

    buyer_changes: list[list[int]] = []
    for nums in buyer_nums:
        add_list = []
        for curr, next in zip(nums, nums[1:]):
            add_list.append(next-curr)
        buyer_changes.append(add_list)

    buyer_seqs: list[dict[tuple[int,...],int]] = []
    seq_len = 4
    for buyer_idx, nums in enumerate(buyer_changes):
        add_dict: dict[tuple[int,...],int] = {}
        for i in range(len(nums) - seq_len + 1):
            seq = tuple(nums[i:i+seq_len])
            if seq not in add_dict:
                add_dict[seq] = buyer_nums[buyer_idx][i + seq_len]
        buyer_seqs.append(add_dict)

    used: set[tuple[int,...]] = set()
    highest = 0

    for seqs in buyer_seqs:
        for seq in seqs:
            if seq in used: 
                continue
            used.add(seq)
            highest = max(highest, count_gain(buyer_seqs, seq))

    return highest

def count_gain(buyer_seqs: list[dict[tuple[int,...],int]], seq: tuple[int,...]) -> int:
    res = 0
    for seqs in buyer_seqs:
        if seq in seqs:
            res += seqs[seq]
    return res

if __name__ == "__main__":
    input_file_dir = "input.txt"
    lines = read_input(input_file_dir)
    
    print(calc_sum(lines, 2000))
    print(most_bananas(lines, 2000))

    
