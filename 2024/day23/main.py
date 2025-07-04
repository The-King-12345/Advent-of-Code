class Node:
    def __init__(self, name):
        self.name = name
        self.connections = set()
    
def read_input(input_file_dir: str) -> list[str]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()

    return lines

def create_nodes(lines: list[str]) -> dict[str, Node]:
    nodes: dict[str, Node] = {}

    for pair in lines:
        a, b = pair.split("-")
        if a not in nodes:
            nodes[a] = Node(a)
        if b not in nodes:
            nodes[b] = Node(b)
        nodes[a].connections.add(nodes[b])
        nodes[b].connections.add(nodes[a])

    return nodes

def get_t_nodes(nodes: dict[str,Node]) -> set[Node]:
    t_nodes: set[Node] = set()
    for node in nodes.values():
        if node.name.startswith("t"):
            t_nodes.add(node)
    return t_nodes

def calc_t_triangles(t_nodes: set[Node]) -> int:
    triangles: set[tuple[int,int,int]] = set()
    
    for t_node in t_nodes:
        dfs(triangles, [t_node], t_node, 3)

    return len(triangles)

def dfs(triangles: set[tuple[int,int,int]], path: list[Node], start_node: Node, depth: int) -> None:
    if depth == 0:
        if path[-1] == start_node:
            triangle = tuple(sorted(node.name for node in path[:-1]))
            if triangle not in triangles:
                triangles.add(triangle)
    else:
        for neighbor in path[-1].connections:
            dfs(triangles, path + [neighbor], start_node, depth - 1)
    return

def calc_password(nodes: dict[str, Node]) -> str:
    passwords: set[str] = set()

    for node in nodes.values():
        build_set(passwords, node, {node})

    return max(passwords, key=len)

def build_set(passwords: set[str], node: Node, group: set[Node]) -> None:
    password = ",".join(sorted(n.name for n in group))
    if password in passwords: return
    passwords.add(password)

    for neighbor in node.connections:
        if neighbor in group: continue
        if any(neighbor not in n.connections for n in group): continue
        build_set(passwords, neighbor, {*group, neighbor})
    return

if __name__ == "__main__":
    input_file_dir = "input.txt"
    lines = read_input(input_file_dir)
    nodes: dict[str, Node] = create_nodes(lines)
    t_nodes: set[Node] = get_t_nodes(nodes)

    print(calc_t_triangles(t_nodes))
    print(calc_password(nodes))
    

    
