import sys

def main():
    # open text file
    in_file_name = sys.argv[1] # 0 = script, 1 = file name
    input_file = open(in_file_name, 'r')
    lines = input_file.readlines()

    # print file
    for line in lines:
        print(line.strip())

    # close file
    input_file.close()

if __name__ == "__main__":
    main()

