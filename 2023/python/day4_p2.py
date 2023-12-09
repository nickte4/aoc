import sys
import numpy

def get_matches_from_card(win_set, have_nums):
    num_matches = 0
    for num in have_nums:
        if num in win_set:
            num_matches += 1
    return num_matches

def get_num_matches(line):
    card_nums = (line[line.find(':') + 2:len(line)]).split(' | ')
    win_nums = (card_nums[0]).split()
    have_nums = (card_nums[1]).split()
    win_set = set(win_nums)

    return get_matches_from_card(win_set, have_nums)
    
def generate_num_matches(lines):
    card_num_matches = []
    for line in lines:
        card_num_matches.append(get_num_matches(line.strip()))

    return card_num_matches

def update_instances(idx, num_card, card_num_instances, card_num_matches):
    for i in range(num_card):
        for j in range(card_num_matches[idx]):
            card_num_instances[idx + j + 1] += 1

def get_total_scratch_cards(card_num_matches, card_num_instances):
    for idx, num_card in enumerate(card_num_instances):
        update_instances(idx, num_card, card_num_instances, card_num_matches)
    return numpy.sum(card_num_instances)

def main():
    # open text file
    in_file_name = sys.argv[1] # 0 = script, 1 = file name
    input_file = open(in_file_name, 'r')
    lines = input_file.readlines()
    
    card_num_matches = generate_num_matches(lines)
    card_num_instances = [1] * len(card_num_matches)

    total_scratch_cards = get_total_scratch_cards(card_num_matches, card_num_instances) 

    print(total_scratch_cards)

    # close file
    input_file.close()

main()


# num matches on each card (marked by idx)
# [ 4, 2, 2, 1, 0, 0]
# num instances of each card 
# [ 1, 1, 1, 1, 1, 1]
# end with 30 cards

