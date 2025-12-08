import sys
import re
from collections import defaultdict

def read_input(input_file_dir: str) -> list[list[str]]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()
    
    problems: list[list[str]] = []

    for line in lines:
        problems.append(re.split(r"[\s]+", line.strip()))
        
    return problems


def read_input2(input_file_dir: str) -> dict[int, list[str]]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()
    
    columns: dict[int, list[str]] = defaultdict(list)

    for line in lines:
        for i, char in enumerate(line):
            columns[i].append(char)
        
    return columns


def calc_grand_total(problems: list[list[str]]) -> int:
    res = 0

    for i in range(len(problems[0])):
        subtot = 1 if problems[-1][i] == "*" else 0

        for problem in problems[:-1]:
            if problems[-1][i] == "*":
                subtot *= int(problem[i])
            else:
                subtot += int(problem[i])

        res += subtot

    return res


def calc_cephalopod_total(columns: dict[int, list[str]]):
    res = 0
    subtot = 0
    plus_flag = False

    for column in columns.values():
        num = ""

        for digit in column[:-1]:
            num += digit

        if num.strip() == "":
            res += subtot
            continue

        if column[-1] == "*":
            subtot = int(num)
            plus_flag = False
        elif column[-1] == "+":
            subtot = int(num)
            plus_flag = True
        else:
            if plus_flag:
                subtot += int(num)
            else:
                subtot *= int(num)

    res += subtot

    return res


if __name__ == "__main__":
    input_file_dir = "input.txt"

    if len(sys.argv) > 1:
        input_file_dir = sys.argv[1]

    problems = read_input(input_file_dir)
    print(calc_grand_total(problems))

    columns = read_input2(input_file_dir)
    print(calc_cephalopod_total(columns))
