def read_input(input_file_dir: str) -> tuple[dict[int, list[int]], list[list[int]]]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()

    rules: dict[int, list[int]] = {}
    page_orders: list[list[int]] = []

    for line in lines:
        if "|" in line:
            nums = line.split("|")
            num1 = int(nums[0])
            num2 = int(nums[1])
            if num1 in rules:
                rules[num1] += [num2]
            else:
                rules[num1] = [num2]

        elif "," in line:
            page_orders += [list(int(n) for n in line.split(","))]

    return rules, page_orders

def calc_valid_middles(rules: dict[int, list[int]], page_orders: list[list[int]]) -> int:
    sum = 0

    for page_order in page_orders:
        if check_valid(rules, page_order):
            sum += get_middle(page_order)

    return sum

def check_valid(rules: dict[int, list[int]], page_order: list[int]) -> bool:
    used: set[int] = set()

    for page in page_order:
        next_pages = rules.get(page, [])

        for next_page in next_pages:
            if next_page in used:
                return False

        used.add(page)

    return True

def get_middle(page_order: list[int]) -> int:
    return page_order[len(page_order)//2]

def calc_invalid_middles(rules: dict[int, list[int]], page_orders: list[list[int]]) -> int:
    sum = 0

    for page_order in page_orders:
        if not check_valid(rules, page_order):
            new_order = make_valid(rules, page_order)
            sum += get_middle(new_order)

    return sum

def make_valid(rules: dict[int, list[int]], page_order: list[int]) -> list[int]:
    used: set[int] = set()

    for page in page_order:
        next_pages = rules.get(page, [])

        for next_page in next_pages:
            if next_page in used:
                new_order = swap_values(page_order, page, next_page)
                return make_valid(rules, new_order)

        used.add(page)

    return page_order

def swap_values(page_order: list[int], page1: int, page2: int) -> list[int]:
    order: list[int] = []

    for page in page_order:
        if page == page1:
            order.append(page2)
        elif page == page2:
            order.append(page1)
        else:
            order.append(page)
    
    return order

if __name__ == "__main__":
    rules, page_orders = read_input("input.txt")
    print(calc_valid_middles(rules, page_orders))
    print(calc_invalid_middles(rules, page_orders))

