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


def answer_count(my_group):

    group_answer_key = []
    for passenger in my_group:
        # parse each yes per passenger to one answer
        passenger = list(passenger)
        # look at each answer individually to add to group key
        for char in passenger:
            if char not in group_answer_key:
                group_answer_key.append(char)


    return len(group_answer_key)


def group_common_count(my_group):

    # create the master list of all yes answers
    group_answer_key = []
    for passenger in my_group:
        # parse each yes per passenger to one answer
        passenger = list(passenger)
        # look at each answer individually to add to group key
        for char in passenger:
            if char not in group_answer_key:
                group_answer_key.append(char)

    # recheck each passenger to against yes list to see if all answered it
    shared_count = 0
    for question in group_answer_key:
        flag = True
        for passenger in my_group:
            if question not in passenger:
                flag = False
                break
        if flag: shared_count += 1

    return shared_count


def main():
    raw_data = read_file('day_06.dat', 'l')

    groups_list = make_groups(raw_data)
    yes_count = 0
    group_common_yes = 0
    for group in groups_list:
        my_yes = answer_count(group)
        my_group_yes = group_common_count(group)
        print(group, my_yes, my_group_yes)
        yes_count += my_yes
        group_common_yes += my_group_yes

    print(f'Total: {yes_count}, Group Common: {group_common_yes}')


if __name__ == '__main__':
    print('Running day 06 directly...')

    main()
