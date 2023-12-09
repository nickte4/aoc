import sys

def get_points_from_card(win_set, have_nums):
    num_of_wins = 0
    for num in have_nums:
        if num in win_set:
            num_of_wins += 1
    if num_of_wins == 0:
        return 0
    else:
        return pow(2, num_of_wins - 1)

def tally_card(line):
    card_nums = (line[line.find(':') + 2:len(line)]).split(' | ')
    win_nums = (card_nums[0]).split()
    have_nums = (card_nums[1]).split()
    win_set = set(win_nums)

    return get_points_from_card(win_set, have_nums)
    

def main():
    # open text file
    in_file_name = sys.argv[1] # 0 = script, 1 = file name
    input_file = open(in_file_name, 'r')
    lines = input_file.readlines()
    
    point_sum = 0

    # print lines
    for line in lines:
        points = tally_card(line.strip())
        point_sum += points

    print(point_sum)

    # close file
    input_file.close()

main()
