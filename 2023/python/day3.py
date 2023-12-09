import sys
import numpy

def check_for_symbol(idx, schematic, line_num, symbol_set):
    symbol_adjacent = False

    # check top
    if line_num - 1 > -1 and schematic[line_num - 1][idx] in symbol_set:
        symbol_adjacent = True

    # check bot
    if line_num + 1 < len(schematic) and schematic[line_num + 1][idx] in symbol_set:
        symbol_adjacent = True

    # check left
    if idx - 1 > -1 and schematic[line_num][idx - 1] in symbol_set:
        symbol_adjacent = True
    
    # check right
    if idx + 1 < len(schematic[0]) and schematic[line_num][idx + 1] in symbol_set:
        symbol_adjacent = True

    # check top-left
    if line_num - 1 > -1 and idx - 1 > -1 and schematic[line_num - 1][idx - 1] in symbol_set:
        symbol_adjacent = True

    # check top-right
    if line_num - 1 > -1 and idx + 1 < len(schematic[0]) and schematic[line_num - 1][idx + 1] in symbol_set:
        symbol_adjacent = True

    # check bot-left
    if line_num + 1 < len(schematic) and idx - 1 > -1 and schematic[line_num + 1][idx - 1] in symbol_set:
        symbol_adjacent = True

    # check bot-right
    if line_num + 1 < len(schematic) and idx + 1 < len(schematic[0]) and schematic[line_num + 1][idx + 1] in symbol_set:
        symbol_adjacent = True

    return symbol_adjacent

def find_part_nums(line, part_nums, schematic, line_num, symbol_set):
    curr_num = []
    is_part_num = False
    for idx, char in enumerate(line):
        if char.isdigit():
            curr_num.append(char)
            if not is_part_num:
                is_part_num = check_for_symbol(idx, schematic, line_num, symbol_set)
        else:
            if is_part_num:
                part_nums.append(int("".join(curr_num)))
            curr_num = []
            is_part_num = False

    if is_part_num:
        part_nums.append(int("".join(curr_num)))

def generate_schematic(lines):
    # convert input into 2d array
    schematic = []
    for line in lines:
        schematic.append(line.strip())
    return schematic

def main():
    symbol_set = {'@', '#', '$', '%', '&', '*', '+', '-', '=', '/'}

    # open file
    in_file_name = sys.argv[1]
    input_file = open(in_file_name, 'r')
    lines = input_file.readlines()
    schematic = generate_schematic(lines)

    sum_engine_nums = 0
    part_nums = []

    # print lines
    for line_num, line in enumerate(schematic):
        find_part_nums(line.strip(), part_nums, schematic, line_num, symbol_set)

    sum_engine_nums = numpy.sum(part_nums)
    print(sum_engine_nums)

    # close file
    input_file.close()

main()

