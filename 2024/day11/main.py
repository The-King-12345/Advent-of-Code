from functools import cache

def read_input(input_file_dir: str) -> list[int]:
    with open(input_file_dir) as f:
        line = f.read().split()

    return list(map(int, line))

def calc_stones(line: list[int], blinks: int) -> int:
    stones = line[:]

    for _ in range(blinks):
        stones = simulate_blink(stones)

    return len(stones)

def simulate_blink(stones: list[int]) -> list[int]:
    res: list[int] = []

    for stone in stones:
        length = len(str(stone))

        if stone == 0:
            res.append(1)
        elif length % 2 == 0:
            res.append(int(str(stone)[:length//2]))
            res.append(int(str(stone)[length//2:]))
        else:
            res.append((stone) * 2024)

    return res

def calc_stones_efficient(line: list[int], blinks: int) -> int:
    res = 0

    for num in line:
        res += blink(num, blinks)

    return res

@cache
def blink(num: int, blinks: int) -> int:
    length = len(str(num))

    if blinks == 1:
        if length % 2 == 0:
            return 2
        else:
            return 1
    
    if num == 0:
        return blink(1, blinks-1)
    elif length % 2 == 0:
        return blink(int(str(num)[:length//2]), blinks-1) + blink(int(str(num)[length//2:]), blinks-1)
    else:
        return blink(num*2024, blinks-1)


if __name__ == "__main__":
    line = read_input("input.txt")
    print(calc_stones(line, 25))
    print(calc_stones_efficient(line, 75))