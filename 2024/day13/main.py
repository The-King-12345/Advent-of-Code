from re import search

def read_input(input_file_dir: str) -> list[list[tuple[int,int]]]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()

    machines = []
    machine = []
    for line in lines:
        if match := search(r"Button A: X\+(\d+), Y\+(\d+)", line):
            machine.append((int(match.group(1)),int(match.group(2))))
        elif match := search(r"Button B: X\+(\d+), Y\+(\d+)", line):
            machine.append((int(match.group(1)),int(match.group(2))))
        elif match := search(r"Prize: X=(\d+), Y=(\d+)", line):
            machine.append((int(match.group(1)),int(match.group(2))))
            machines.append(machine)
            machine = []

    return machines

def calc_fewest_tokens(machines: list[list[tuple[int,int]]], offset: int) -> int:
    res = 0
    
    for machine in machines:
        xa, ya = machine[0]
        xb, yb = machine[1]
        xc, yc = machine[2]
        xc += offset
        yc += offset

        denom = xa * yb - ya * xb
        if denom != 0:
            a: float = (xc * yb - yc * xb) / denom
            b: float = (xa * yc - ya * xc) / denom
        else:
            a = -1
            b = -1

        if a >= 0 and b >= 0 and a.is_integer() and b.is_integer():
            res += int(a) * 3 + int(b)

    return res

if __name__ == "__main__":
    machines = read_input("input.txt")
    print(calc_fewest_tokens(machines,0))
    print(calc_fewest_tokens(machines,10000000000000))


