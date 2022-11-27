from shared_use import read_file


def make_groups(my_raw_data):
    # create empty list to hold groups
    clean_list = []

    # we need an empty line at end of list to mark finish, add that if not here
    if my_raw_data[-1] != '':
        my_raw_data.append('')

    # loop through all items, create temp 1-d list
    # for each group, strip empty lines and push the
    # new list to the clean list (create 2-d list of each
    # group in sub-list)
    temp_group = []
    for i in range(len(my_raw_data)):
        # check first to see if we are between groups, if so record
        # data and clean up temp group
        if my_raw_data[i] == '':
            # create copy to avoid later .clear() problems in clean list
            ls = temp_group.copy()
            clean_list.append(ls)
            temp_group.clear()
            continue
        # if we have a passenger, record them in the temp group and move to next
        temp_group.append(my_raw_data[i])

    return clean_list


def asnwer_count(my_group):



def main():
    raw_data = read_file('test.dat', 'l')
    print(raw_data)

    groups_list = make_groups(raw_data)
    yes_count = 0
    for group in groups_list:
        print(group)
        yes_count += answer_count(group)


if __name__ == '__main__':
    print('Running day 06 directly...')

    main()
