import sys
import numpy

def check_for_symbol(idx, schematic, line_num):
    star_key = ""

    # check top
    if line_num - 1 > -1 and schematic[line_num - 1][idx] == '*':
        star_key = str(line_num - 1) + "," + str(idx)

    # check bot
    if line_num + 1 < len(schematic) and schematic[line_num + 1][idx] == '*':
        star_key = str(line_num + 1) + "," + str(idx)

    # check left
    if idx - 1 > -1 and schematic[line_num][idx - 1] == '*':
        star_key = str(line_num) + "," + str(idx - 1)
    
    # check right
    if idx + 1 < len(schematic[0]) and schematic[line_num][idx + 1] == '*':
        star_key = str(line_num) + "," + str(idx + 1)

    # check top-left
    if line_num - 1 > -1 and idx - 1 > -1 and schematic[line_num - 1][idx - 1] == '*':
        star_key = str(line_num - 1) + "," + str(idx - 1)

    # check top-right
    if line_num - 1 > -1 and idx + 1 < len(schematic[0]) and schematic[line_num - 1][idx + 1] == '*':
        star_key = str(line_num - 1) + "," + str(idx + 1)

    # check bot-left
    if line_num + 1 < len(schematic) and idx - 1 > -1 and schematic[line_num + 1][idx - 1] == '*':
        star_key = str(line_num + 1) + "," + str(idx - 1)

    # check bot-right
    if line_num + 1 < len(schematic) and idx + 1 < len(schematic[0]) and schematic[line_num + 1][idx + 1] == '*':
        star_key = str(line_num + 1) + "," + str(idx + 1)

    return star_key

def add_part_to_map(part_num, star_map, star_key):
    if star_key in star_map:
        star_map[star_key].append(part_num)
    else:
        star_map[star_key] = []
        star_map[star_key].append(part_num)

def find_part_nums(line, schematic, line_num, star_map):
    curr_num = []
    star_key = ""
    for idx, char in enumerate(line):
        if char.isdigit():
            curr_num.append(char)
            if star_key == "":
                star_key = check_for_symbol(idx, schematic, line_num)
        else:
            if star_key != "":
                part_num = int("".join(curr_num))
                add_part_to_map(part_num, star_map, star_key)
            curr_num = []
            star_key = ""
            
    if star_key != "":
        part_num = int("".join(curr_num))
        add_part_to_map(part_num, star_map, star_key)

def generate_schematic(lines):
    # convert input into 2d array
    schematic = []
    for line in lines:
        schematic.append(line.strip())
    return schematic

def main():
    star_map = {}
    # open file
    in_file_name = sys.argv[1]
    input_file = open(in_file_name, 'r')
    lines = input_file.readlines()
    schematic = generate_schematic(lines)

    sum_engine_nums = 0

    # print lines
    for line_num, line in enumerate(schematic):
        find_part_nums(line.strip(), schematic, line_num, star_map)

    for val in star_map.values():
        if len(val) == 2:
            sum_engine_nums += numpy.prod(val)


    print(sum_engine_nums)

    # close file
    input_file.close()

main()







