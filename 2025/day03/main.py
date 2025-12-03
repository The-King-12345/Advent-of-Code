def read_input(input_file_dir: str) -> list[list[int]]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()
    
    res: list[list[int]] = []

    for line in lines:
        res.append([int(val) for val in line])
    
    return res


def calc_total_joltage(banks: list[list[int]], amount: int) -> int:
    res = 0

    for bank in banks:
        res += get_bank_joltage(bank, amount)

    return res


def get_bank_joltage(bank: list[int], amount: int) -> int:
    res = ""
    prev = 0

    for i in range(amount):
        p1 = find_largest(bank, prev, len(bank)-amount+1+i)
        prev = p1 + 1
        res += str(bank[p1])

    return int(res)


def find_largest(arr: list[int], start: int, end: int):
    largest_val = arr[start]
    largest_i = start

    for i in range(start,end):
        if arr[i] > largest_val:
            largest_val = arr[i]
            largest_i = i

    return largest_i


if __name__ == "__main__":
    input_file_dir = "input.txt"
    banks = read_input(input_file_dir)

    print(calc_total_joltage(banks, 2))
    print(calc_total_joltage(banks, 12))
    