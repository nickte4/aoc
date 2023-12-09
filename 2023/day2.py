import sys

TOTAL_RED = 12
TOTAL_GREEN = 13
TOTAL_BLUE = 14

def get_game_id(game_name):
    idx_of_id = -1;
    for i, c in enumerate(game_name):
        if c.isdigit():
            idx_of_id = i
            break

    return int(game_name[idx_of_id:len(game_name)])

def check_cube(cube):
    is_possible = False
    if cube.find("red") != -1:
        num_cube = int(cube[0:cube.find(" red")])
        is_possible = num_cube <= TOTAL_RED
    elif cube.find("blue") != -1:
        num_cube = int(cube[0:cube.find(" blue")])
        is_possible = num_cube <= TOTAL_BLUE
    else:
        num_cube = int(cube[0:cube.find(" green")])
        is_possible = num_cube <= TOTAL_GREEN

    return is_possible


def check_set(curr_set):
    cubes = curr_set.split(', ')
    for cube in cubes:
        if not check_cube(cube):
            return False
    return True

def check_game(game_set):
    for curr_set in game_set:
        if not check_set(curr_set):
            return False
    return True

def parse_game(game_line):
    # split line into separate sets
    game_set = game_line.split('; ')

    # get game id
    game_elems = game_set[0].split(': ')
    game_name = game_elems[0]
    game_id = get_game_id(game_name)

    # replace first element with first set
    game_set[0] = game_elems[1]

    # check if the game sets are correct
    if check_game(game_set):
        return game_id

    # impossible game
    return -1

def main():
    # open file
    in_file_name = sys.argv[1]
    input_file = open(in_file_name, 'r')
    lines = input_file.readlines()
    
    print(f"bag: {TOTAL_RED} red cubes, {TOTAL_GREEN} green cubes, {TOTAL_BLUE} blue cubes\n")

    id_sum = 0
    # print lines
    for line in lines:
        print(line.strip())
        game_id = parse_game(line.strip())
        if game_id != -1:
            id_sum += game_id

    print(id_sum)

    # close file
    input_file.close()

main()
