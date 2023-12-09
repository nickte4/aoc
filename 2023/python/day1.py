import sys # for arg reading

nums = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def find_first_digit(line):
    possible_nums = nums.keys()
    num_str_idx = 99999 # need a ceiling value
    num_str = ""
    first_digit = ""
    digit = ""

    for curr_num in possible_nums:
        found_num_idx = line.find(curr_num)
        if found_num_idx < num_str_idx and found_num_idx != -1:
            num_str_idx = found_num_idx
            num_str = curr_num

    for char in line:
        if char.isnumeric():
            digit = char
            break

    if line.find(digit) != -1 and line.find(digit) < num_str_idx:
        first_digit = digit
    elif num_str_idx != -1:
        first_digit = nums[num_str]
    
    return first_digit

def find_last_digit(line):
    possible_nums = nums.keys()
    num_str_idx = -1
    num_str = ""
    last_digit = ""
    digit = ""

    for curr_num in possible_nums:
        found_num_idx = line.rfind(curr_num)
        if found_num_idx > num_str_idx:
            num_str_idx = found_num_idx
            num_str = curr_num

    for char in reversed(line):
        if char.isnumeric():
            digit = char
            break

    
    if line.rfind(digit) != -1 and line.rfind(digit) > num_str_idx and digit != "":
        last_digit = digit
    elif num_str_idx != -1:
        last_digit = nums[num_str]

    return last_digit


def return_arr_sum(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum

def fill_arr(lines, arr):
    # fill calibration_values
    for line in lines:
        first_digit = find_first_digit(line)
        last_digit = find_last_digit(line)
        arr.append(first_digit + last_digit)

def main():
    # open text file
    in_file_name = sys.argv[1] # 0 = script, 1 = file name
    input_file = open(in_file_name, 'r')
    lines = input_file.readlines()

    # collection of all calib. values
    calibration_values = []
    fill_arr(lines, calibration_values)
    calibration_values = [ int(x) for x in calibration_values ]

    # print(calibration_values)
    print(return_arr_sum(calibration_values))

    # close file
    input_file.close()

main()
