def read_input(input_file_dir: str) -> list[list[list[int]]]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()
    
    res: list[list[list[int]]] = []

    for line in lines:
        temp_game: list[list[int]] = []

        _, info = line.split(": ")
        throws = info.split("; ")
        
        for throw in throws:
            dice = throw.split(", ")

            temp_line: list[int] = [0,0,0]

            for die in dice:
                num, color = die.split(" ")
                
                if color == "red":
                    temp_line[0] = int(num)
                elif color == "green":
                    temp_line[1] = int(num)
                elif color == "blue":
                    temp_line[2] = int(num)

            temp_game.append(temp_line)

        res.append(temp_game)
        
    return res


def calc_possible(games: list[list[list[int]]], red: int, green: int, blue: int) -> int:
    res = 0

    for i, game in enumerate(games):
        id = i + 1
        
        if is_possible(game, red, green, blue):
            res += id

    return res


def is_possible(game: list[list[int]], red: int, green: int, blue: int) -> bool:
    for throw in game:
        if throw[0] > red or throw[1] > green or throw[2] > blue: 
            return False
    
    return True


def calc_minimum(games: list[list[list[int]]]) -> int:
    res = 0

    for game in games:
        res += find_power(game)

    return res


def find_power(game: list[list[int]]) -> int:
    min_red = 0
    min_green = 0
    min_blue = 0

    for throw in game:
        if throw[0] > min_red:
            min_red = throw[0]
        if throw[1] > min_green:
            min_green = throw[1]
        if throw[2] > min_blue:
            min_blue = throw[2]

    res = min_red * min_green * min_blue
    return res


if __name__ == "__main__":
    input_file_dir = "input.txt"
    games = read_input(input_file_dir)
    print(calc_possible(games, 12, 13, 14))
    print(calc_minimum(games))
    