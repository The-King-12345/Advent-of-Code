def read_input(input_file_dir: str) -> list[tuple[int, int]]:
    with open(input_file_dir) as f:
        ranges = f.read().split(",")
    
    res: list[tuple[int, int]] = []

    for range in ranges:
        low, high = range.split("-")
        res.append((int(low), int(high)))
    
    return res


def is_invalid(num: int) -> bool:
    val = str(num)

    for i in range(1, len(val) // 2 + 1):
        if val == val[:i] * 2:
            return True

    return False

def sum_invalid(ranges: list[tuple[int, int]]) -> int:
    res = 0

    for low, high in ranges:
        for num in range(low, high+1):
            if is_invalid(num):
                res += num

    return res


def is_new_invalid(num: int) -> bool:
    val = str(num)

    for i in range(1, len(val) // 2 + 1):
        for k in range(1, len(val) // len(val[:i]) + 1):
            if val == val[:i] * k:
                return True

    return False


def sum_new_invalid(ranges: list[tuple[int, int]]) -> int:
    res = 0

    for low, high in ranges:
        for num in range(low, high+1):
            if is_new_invalid(num):
                res += num

    return res


if __name__ == "__main__":
    input_file_dir = "input.txt"
    ranges = read_input(input_file_dir)
    print(sum_invalid(ranges))
    print(sum_new_invalid(ranges))
