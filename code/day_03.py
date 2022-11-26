# file i/o
def read_file(filename):
    filename = 'code/' + filename
    with open(filename, 'r') as inf:
        my_raw_data = [line for line in inf.read().split('\n')]
    return my_raw_data


def show_sled(my_map):
    map_w = len(my_map[0])
    map_h = len(my_map)

    print_w = int(int(3*map_h)/map_w)
    for i in range(map_h):
        for j in range(print_w):
            print(my_map[i], end='')
        print()


def find_sled(my_map, my_rise, my_run):
    my_hit_total = 0
    my_x = 0

    print(f'Checking slope {my_rise} by {my_run}')
    for i in range(0, len(my_map), my_rise):
        # print(f'Checking ({my_x}, {i})-{my_map[i][my_x]}')
        if my_map[i][my_x] == '#':
            my_hit_total += 1
        my_x += my_run
        if my_x >= len(my_map[0]):
            my_x -= len(my_map[0])

    print(f'Found {my_hit_total} tree collisions.')
    return my_hit_total


def main():

    raw_data = read_file('../dat/day_03.dat')
    print(raw_data)
    # show_sled(raw_data)

    total = 1
    total *= find_sled(raw_data, 1, 1)
    print(f'Total: {total}')
    total *= find_sled(raw_data, 1, 3)
    print(f'Total: {total}')
    total *= find_sled(raw_data, 1, 5)
    print(f'Total: {total}')
    total *= find_sled(raw_data, 1, 7)
    print(f'Total: {total}')
    total *= find_sled(raw_data, 2, 1)
    print(f'Total: {total}')

    print(f'Total: {total}')
