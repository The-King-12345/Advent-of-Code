from itertools import product

def read_input(input_file_dir: str) -> list[list[int]]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()

    equations: list[list[int]] = []

    for line in lines:
        answer, expression = line.split(":")
        nums = expression.split()
        equations.append([int(answer)] + [int(n) for n in nums])

    return equations

def calc_total_calibration(lines: list[list[int]], iterables: list[int]) -> int:
    sum = 0

    for line in lines:
        if is_valid(line[0], line[1:], iterables):
            sum += line[0]

    return sum

def is_valid(answer: int, nums: list[int], iterables: list[int]) -> bool:
    target_length = len(nums) - 1
    combos = [list(combo) for combo in product(iterables, repeat=(target_length))]

    for operators in combos:
        if evaluate_expression(nums, operators) == answer:
            return True

    return False    

def evaluate_expression(nums: list[int], operators: list[int]) -> int:
    res = nums[0]
    
    for i, num in enumerate(nums[1:]):
        if operators[i] == 0:
            res += num
        elif operators[i] == 1:
            res *= num
        else:
            res = int(str(res) + str(num))

    return res

if __name__ == "__main__":
    lines = read_input("input.txt")
    print(calc_total_calibration(lines, [0,1]))
    print(calc_total_calibration(lines, [0,1,2]))




