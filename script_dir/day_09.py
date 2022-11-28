from shared_use import read_file


def check(my_data):

    # define cypher lengths
    cypher_len = 25
    preamble = 25

    # start check after preamble (index is at preamble since index[0])
    current = preamble

    dpass = True
    while dpass:
        lpass = False
        first = current - cypher_len
        print(f'Checking {my_data[current]}...', end=' ')
        for i in range(first, current):
            if lpass: break
            for j in range(i+1, current):
                if lpass: break
                if my_data[i] + my_data[j] == my_data[current]:
                    print(f'found {my_data[i]}+{my_data[j]}={my_data[current]}')
                    current += 1
                    lpass = True
                    if current >= len(my_data):
                        print('Checked all data, valid data set!')
                        dpass = False
                    continue
        if not lpass:
            print(f'{my_data[current]} does not appear to be a valid data point!')
            dpass = False

    decrypt(my_data, current)


def decrypt(my_data, my_target):
    first = 0

    done = False
    while not done:
        sum = 0
        i = first
        while sum < my_data[my_target]:
            sum += my_data[i]
            i += 1
            if sum == my_data[my_target]:
                done = True
        if not done:
            first += 1

    print(f'Found sequence from index {first} to {i}')
    decrypted_sequence = my_data[first:i]
    for num in decrypted_sequence:
        print(f'{num}+', end='')
    print(f'={my_data[my_target]}')

    decrypted_sequence.sort()
    print(f'{decrypted_sequence[-1]}+{decrypted_sequence[0]}={decrypted_sequence[-1]+decrypted_sequence[0]}')




def main():
    raw_data = read_file('day_09.dat', 'l')
    # force list to int type for easier maths later
    raw_data = [int(x) for x in raw_data]

    check(raw_data)
    return


if __name__ == '__main__':
    print('running day 9 directly')
    main()
