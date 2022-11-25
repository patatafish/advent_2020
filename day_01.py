# file io
def read_file(filename):
    with open(filename, 'r') as inf:
        raw_data = [line for line in inf.read().split("\n")]
    return raw_data


if __name__ == '__main__':

    raw_data = read_file('day_01.dat')
    print(raw_data)

    my_len = len(raw_data)

    flag = False
    for i in range(my_len):
        if flag: break
        for j in range(i+1, my_len):
            my_i = int(raw_data[i])
            my_j = int(raw_data[j])
            my_sum = my_i + my_j
            if my_sum == 2020:
                print(f'{my_i}+{my_j}={my_sum}')
                flag = True
                break

    print(f'Found: {my_i * my_j}')

    flag = False
    for i in range(my_len):
        if flag: break
        for j in range(i+1, my_len):
            if flag: break
            for k in range(j+1, my_len):
                my_i = int(raw_data[i])
                my_j = int(raw_data[j])
                my_k = int(raw_data[k])
                my_sum = my_i + my_j + my_k
                if my_sum == 2020:
                    print(f'{my_i}+{my_j}+{my_k}={my_sum}')
                    flag = True
                    break

    print(f'Found {my_i * my_j * my_k}')