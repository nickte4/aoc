import sys

def parse_line(line, map_range):
    print(line)
    
def parse_seed_map(line, map_range):
    seed_nums = (line.split(" "))[1:]
    seed_array = [int(seed_num) for seed_num in seed_nums]
    map_range['seeds'] = seed_array

def parse_map(lines):
    map_range = {}
    parse_seed_map(lines[0].strip(), map_range)
    lines = lines[1:] # remove first seed line
    for line in lines:
        if line.strip() != "":
            parse_line(line.strip(), map_range)


def parse_file():
    # open text file
    in_file_name = sys.argv[1] # 0 = script, 1 = file name
    input_file = open(in_file_name, 'r')
    text = input_file.readlines()
    # close file
    input_file.close()
    return text

def main():
    lines = parse_file()
    # parse seed file
    parse_map(lines)

if __name__ == "__main__":
    main()

# seeds: 79 14 55 13
#
#   range: 2
#   src: 98 - 99
#   dest: 50 - 51 
#
#   range: 48
#   src: 50 - 97
#   dest: 52 - 99
#
#   everything else:
#   src: 0 - 49
#   dest: 0 - 49
#  
# seed-to-soil: 79->81, 14->14, 55->57, 13->13
