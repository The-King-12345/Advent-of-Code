from re import search

def read_input(input_file_dir: str) -> tuple[list[int],int,int,int]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()

    program: list[int] = []

    for line in lines:
        if match := search(r"Register A: (\d+)", line):
            reg_a = int(match.group(1))
        elif match := search(r"Register B: (\d+)", line):
            reg_b = int(match.group(1))
        elif match := search(r"Register C: (\d+)", line):
            reg_c = int(match.group(1))
        elif match := search(r"Program: (.+)", line):
            program = list(map(int, match.group(1).split(",")))
            
    return program, reg_a, reg_b, reg_c

def find_output(program: list[int], reg_a: int, reg_b: int = 0, reg_c: int = 0) -> str:
    output: list[int] = []
    pointer = 0

    a, b, c = [reg_a], [reg_b], [reg_c]
    combos: dict[int, list[int]] = {0: [0], 1:[1], 2:[2], 3:[3], 4:a, 5:b, 6:c}

    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer+1]
        combo = combos[operand][0]

        if opcode == 0: 
            # bitwise shift equivalent to int(a[0] / 2**combo)
            a[0] = a[0] >> combo 
        elif opcode == 1:
            b[0] = b[0] ^ operand
        elif opcode == 2:
            b[0] = combo % 8
        elif opcode == 3:
            if a[0] != 0:
                pointer = operand
                continue
        elif opcode == 4:
            b[0] = b[0] ^ c[0]
        elif opcode == 5:
            output.append(combo % 8)
        elif opcode == 6:
            b[0] = a[0] >> combo
        elif opcode == 7:
            c[0] = a[0] >> combo

        pointer += 2

    return ",".join(str(n) for n in output)

def find_lowest_copy(program: list[int]) -> int:
    # Only works for input.txt
    # Program: 2,4,1,1,7,5,1,5,0,3,4,3,5,5,3,0
    # b = a
    # b = b ^ 1
    # c = a >> b
    # b = b ^ 5
    # a = a >> 3    ***Important Line
    # b = b ^ c

    solutions: set[str] = set()
    add_list: set[str] = set()

    for i in range(1,17):
        if i == 1:
            for new_part in range(8):
                if find_output(program, int(f"{new_part:03b}", 2)) == ",".join(str(n) for n in program[-i:]):
                    solutions.add(f"{new_part:03b}")
        else:
            while solutions:
                previous = solutions.pop()
                
                for new_part in range(8):
                    if find_output(program, int(previous + f"{new_part:03b}", 2)) == ",".join(str(n) for n in program[-i:]):
                        add_list.add(previous + f"{new_part:03b}")

            solutions.update(add_list)
            add_list.clear()

    min = float("inf")

    for solution in solutions:
        if int(solution, 2) < min:
            min = int(solution, 2)

    return int(min)

if __name__ == "__main__":
    input_file_dir = "input.txt"
    program, reg_a, reg_b, reg_c = read_input(input_file_dir)
    print(find_output(program, reg_a, reg_b, reg_c))
    if input_file_dir == "input.txt":
        print(find_lowest_copy(program))

    