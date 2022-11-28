import copy

from shared_use import read_file

def run_code(my_code):
    # create copy of code, so we don't alter the original
    new_code = copy.deepcopy(my_code)
    acc = 0
    line = 0

    while True:
        # print(my_code[line])
        if line >= len(new_code):
            print(f'Program finished, accumulator at {acc}')
            return 1
        elif new_code[line][0]:
            print(f'Found loop, exiting with accumulator at {acc}')
            return 0
        elif new_code[line][1] == 'nop':
            new_code[line][0] = 1
            line += 1
            continue
        elif new_code[line][1] == 'acc':
            new_code[line][0] = 1
            acc += int(new_code[line][2])
            line += 1
            continue
        elif new_code[line][1] == 'jmp':
            new_code[line][0] = 1
            line += int(new_code[line][2])
            continue


def clean(my_data):
    full_code = []

    for inst in my_data:
        clean_line = inst.split(' ')
        clean_line.insert(0, None)
        full_code.append(clean_line)

    return full_code


def clean_loop(my_data):

    super_clean = copy.deepcopy(my_data)
    check_list = []
    line = 0
    # mark all execulted code lines
    print('Marking loop...')
    while not my_data[line][0]:
        my_data[line][0] = 1
        if my_data[line][1] == 'jmp':
            line += int(my_data[line][2])
        else:
            line += 1

    # create list of all 'jmp' and 'nop' lines
    print('Identifying culprits...')
    for i in range(len(my_data)):
        if not my_data[i][0]:
            continue

        if any(x in ['jmp', 'nop'] for x in my_data[i]):
            check_list.append(i)

    print(f'Found {len(check_list)} items to check...\n')

    # iterate the check list, running code each time to see if we loop or not
    for i in check_list:
        # create a copy of the OG code, use that for swap check
        altered_code = copy.deepcopy(super_clean)
        # clean the leading 1 so we can test the run

        print(f'{i}: {altered_code[i]} => ', end='')
        if 'jmp' in altered_code[i]:
            altered_code[i][1] = altered_code[i][1].replace('jmp', 'nop')
        else:
            altered_code[i][1] = altered_code[i][1].replace('nop', 'jmp')
        print(f'{altered_code[i]}')

        if run_code(altered_code):
            print(f'I think changing line {i} fixes the loop!')
            return


def main():
    raw_data = read_file('day_08.dat', 'l')

    full_code = clean(raw_data)
    run_code(full_code)
    clean_loop(full_code)


if __name__ == '__main__':
    print('Running day 8 directly')
    main()