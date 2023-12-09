import sys
import numpy

# set indices of max red in the min_color_arr
MAX_RED, MAX_BLUE, MAX_GREEN = 0, 1, 2

def get_game_id(game_name):
    idx_of_id = -1;
    for i, c in enumerate(game_name):
        if c.isdigit():
            idx_of_id = i
            break

    return int(game_name[idx_of_id:len(game_name)])

def check_cube(cube, min_color_arr):
    # min_color_arr = [MAX_RED, MAX_BLUE, MAX_GREEN]
    if cube.find("red") != -1:
        num_cube = int(cube[0:cube.find(" red")])
        if num_cube > min_color_arr[MAX_RED]:
            min_color_arr[MAX_RED] = num_cube

    elif cube.find("blue") != -1:
        num_cube = int(cube[0:cube.find(" blue")])
        if num_cube > min_color_arr[MAX_BLUE]:
            min_color_arr[MAX_BLUE] = num_cube
    else:
        num_cube = int(cube[0:cube.find(" green")])
        if num_cube > min_color_arr[MAX_GREEN]:
            min_color_arr[MAX_GREEN] = num_cube

def check_set(curr_set, min_color_arr):
    cubes = curr_set.split(', ')
    for cube in cubes:
        check_cube(cube, min_color_arr)

def check_game(game_set):
    min_color_arr = [0, 0, 0]
    for curr_set in game_set:
        check_set(curr_set, min_color_arr)
    return min_color_arr

def parse_game(game_line):
    # split line into separate sets
    game_set = game_line.split('; ')

    # get game id
    game_elems = game_set[0].split(': ')
    game_name = game_elems[0]
    game_id = get_game_id(game_name)

    # replace first element with first set
    game_set[0] = game_elems[1]

    # get min_color_arr
    return check_game(game_set)

def main():
    # open file
    in_file_name = sys.argv[1]
    input_file = open(in_file_name, 'r')
    lines = input_file.readlines()
    sum_of_power_sets = 0

    # print lines
    for line in lines:
        curr_min_color_arr = parse_game(line.strip())
        sum_of_power_sets += numpy.prod(curr_min_color_arr) 

    print(sum_of_power_sets)

    # close file
    input_file.close()

main()
