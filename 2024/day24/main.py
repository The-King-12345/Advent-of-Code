from re import search

class Gate:
    def __init__(self, ins: list[str], op: str , out: str) -> None:
        self.ins: list[str] = ins
        self.op: str = op
        self.out: str = out
 
    def change_out(self, out: str) -> None:
        self.out = out

    def __str__(self) -> str:
        return f"{self.out} = {self.ins[0]} {self.op} {self.ins[1]}"

def read_input(input_file_dir: str) -> tuple[dict[str,int], dict[str, Gate]]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()

    wires: dict[str,int] = {}
    gates: dict[str, Gate] = {}

    for line in lines:
        if match := search(r"((?:x|y)\d\d): (0|1)", line):
            wires[match.group(1)] = int(match.group(2))
        if match := search(r"(...) (AND|XOR|OR) (...) -> (...)", line):
            gates[match.group(4)] = Gate([match.group(1),match.group(3)],match.group(2),match.group(4))

    return wires, gates

def calc_z_output(wires: dict[str,int], gates: dict[str, Gate]) -> int:
    queue = list(gates.values())

    while queue:
        gate = queue.pop(0)
        if gate.ins[0] not in wires or gate.ins[1] not in wires:
            queue.append(gate)
            continue
        if gate.op == "AND":
            wires[gate.out] = wires[gate.ins[0]] and wires[gate.ins[1]]
        elif gate.op == "OR":
            wires[gate.out] = wires[gate.ins[0]] or wires[gate.ins[1]]
        elif gate.op == "XOR":
            wires[gate.out] = wires[gate.ins[0]] ^ wires[gate.ins[1]]

    bin_list: list[tuple[str,str]] = []
    for wire, value in wires.items():
        if wire.startswith("z"):
            bin_list.append((wire, str(value)))

    return int("".join([item[1] for item in sorted(bin_list,reverse=True)]),2)

def calc_swapped_wires(gates: dict[str,Gate]) -> str:
    z_wires: list[str] = [key for key in sorted(gates.keys()) if key.startswith("z")]
    res: list[str] = []

    for z_wire in z_wires[2:-1]:
        res += fix_wire(gates, z_wire)

    return ",".join(sorted(res))

def fix_wire(gates: dict[str,Gate], z_wire: str) -> list[str]:
    # zn = nxor XOR m1
    # nxor = xn XOR yn
    # m1 = m2 OR prevand
    # prevand = xn-1 AND yn-1
    # m2 = prevxor AND (something else from prev)
    # prevxor = xn-1 XOR yn-1

    num = f"{int(z_wire[1:]):02d}"
    prev_num = f"{int(z_wire[1:])-1:02d}"

    to_swap: list[str] = []
    prevand = find_gate(gates, op="AND", in1="x"+prev_num, in2="y"+prev_num)
    prevxor = find_gate(gates, op="XOR", in1="x"+prev_num, in2="y"+prev_num)
    m2 = find_gate(gates, op="AND", in1=prevxor.out)
    m1 = find_gate(gates, op="OR", in1=m2.out, in2=prevand.out)
    nxor = find_gate(gates, "XOR", in1="x"+num, in2="y"+num)
    zn = find_gate(gates, op="XOR", in1=nxor.out, in2=m1.out)
    if zn is None:
        zn = gates[z_wire]
        to_swap = list(set(zn.ins) ^ set([nxor.out, m1.out]))
    if zn.out != z_wire:
        to_swap = [z_wire, zn.out]
    if to_swap:
        swap(gates, *to_swap)
    return to_swap

def find_gate(gates: dict[str,Gate], op: str, in1: str|None = None, in2: str|None = None):
    for gate in gates.values():
        if op != gate.op: continue
        if in1 and in1 not in gate.ins: continue
        if in2 and in2 not in gate.ins: continue
        return gate
    return None

def swap(gates: dict[str,Gate], w1: str, w2: str) -> None:
    gates[w1], gates[w2] = gates[w2], gates[w1]
    gates[w1].change_out(w1)
    gates[w2].change_out(w2)
    
if __name__ == "__main__":
    input_file_dir = "input.txt"
    wires, gates = read_input(input_file_dir)
    print(calc_z_output(wires, gates))
    if input_file_dir == "input.txt":
        print(calc_swapped_wires(gates))



    
