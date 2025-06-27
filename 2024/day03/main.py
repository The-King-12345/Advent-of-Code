import re

def read_input(input_file_dir: str) -> str:
    with open(input_file_dir) as f:
        text = f.read()
    return text

def calc_mul_statements(text: str) -> int:
    sum = 0
    matches = re.findall(r"mul\((\d+),(\d+)\)", text)
    for match in matches:
        sum += int(match[0]) * int(match[1])

    return sum

def calc_mul_statements_with_do(text: str) -> int:
    sum = 0
    do = True

    matches = re.findall(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", text)
    for match in matches:
        if match[0] == "do()":
            do = True
        elif match[0] == "don't()":
            do = False
        else:
            if do:
                sum += int(match[1]) * int(match[2])
    return sum

if __name__ == "__main__":
    text = read_input("input.txt")
    print(calc_mul_statements(text))
    print(calc_mul_statements_with_do(text))