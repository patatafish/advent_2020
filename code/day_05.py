from shared_use import read_file

def get_seat(my_ticket):
    binary_ticket = ''
    for i in range(len(my_ticket)):
        if my_ticket[i] in ['B', 'R']:
            binary_ticket += '1'
        else:
            binary_ticket += '0'
    my_row = int(binary_ticket[:7], 2)
    my_col = int(binary_ticket[7:], 2)

    return [my_row, my_col]


def your_seat(my_seat_list):
    my_seat_list.sort()
    for i in range(len(my_seat_list)):
        if my_seat_list[i+1] - my_seat_list[i] != 1:
            print(f'Your seat: {my_seat_list[i] + 1}')
            break



def main():
    raw_data = read_file('day_05.dat', 'l')
    print(raw_data)

    highest = 0
    seat_id_list = []
    for ticket in raw_data:
        seat_info = get_seat(ticket)
        seat_id = (seat_info[0] * 8) + seat_info[1]
        seat_id_list.append(seat_id)
        print(f'{ticket}, row={seat_info[0]}, column={seat_info[1]}, seat={seat_id}')
        if seat_id > highest:
            highest = seat_id

    print(f'Highest: {highest}')

    your_seat(seat_id_list)


if __name__ == '__main__':
    print('running from day_05.py')
    main()