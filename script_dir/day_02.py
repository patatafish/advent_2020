# file io
def read_file(filename):
    filename = 'script_dir/' + filename
    with open(filename, 'r') as inf:
        my_raw_data = [line for line in inf.read().split("\n")]
    return my_raw_data


def clean_up_data(my_raw_data):
    my_clean_data = []
    for line in my_raw_data:
        raw_items = line.split(' ')
        range_low, range_high = raw_items[0].split('-')
        target_char = raw_items[1][0]
        my_clean_line = [range_low, range_high, target_char, raw_items[2]]
        # print(my_clean_line)
        my_clean_data.append(my_clean_line)

    return my_clean_data


def check_password(my_line):
    this_len = len(my_line[3])
    print(my_line, this_len)
    my_count = 0
    for my_char in my_line[3]:
        if my_char == my_line[2]:
            my_count += 1
    # print(f'Found {my_count} of {my_line[2]} in {my_line[3]}')
    if int(my_line[0]) <= int(my_count) <= int(my_line[1]):
        return 1
    else:
        return 0


def check_b_password(my_line):
    count = 0
    print(f'{my_line[2]}: {my_line[3][int(my_line[0])-1]}, {my_line[3][int(my_line[1])-1]}')
    if my_line[3][int(my_line[0])-1] == my_line[2]:
        # print(f'found {my_line[2]} at pos {int(my_line[0])-1}')
        count += 1
    if my_line[3][int(my_line[1])-1] == my_line[2]:
        # print(f'did not see {my_line[2]} at pos {int(my_line[1])-1}')
        count += 1

    if count == 1:
        return 1
    return 0


def main():

    raw_data = read_file('../dat/day_02.dat')
    print(raw_data)
    clean_data = clean_up_data(raw_data)

    clean_count = 0
    clean_count_b = 0
    for checks in clean_data:
        clean_count += check_password(checks)
        clean_count_b += check_b_password(checks)

    print(f'Found {clean_count} clean passwords.')
    print(f'Found {clean_count_b} clean b passwords.')
