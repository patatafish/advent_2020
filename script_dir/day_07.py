from shared_use import read_file


def pack_luggage(new_bag, my_luggage):
    clean_new_bag = ['none', []]

    # parse out to individual words for packing
    new_bag = new_bag.split(' ')
    clean_new_bag[0] = (str(new_bag[0] + ' ' + new_bag[1]))

    # delete name of our bag to look for any contents
    del new_bag[0:4]
    while new_bag:
        try:
            int(new_bag[0])
            contain_num = new_bag[0]
            contain_name = str(new_bag[1] + ' ' + new_bag[2])
            clean_new_bag[1].append([contain_num, contain_name])
            del new_bag[0:4]
        except:
            new_bag.clear()
            continue


    print(clean_new_bag)
    my_luggage.append(clean_new_bag)

    return my_luggage


def count_luggage(target, my_luggage):
    print(f'Counting {target}...')
    container_list = [target]

    # count for total number of bags
    flag = True

    while flag:
        print(f'===Current list:{container_list}')
        # set exit flag, changed if we find targets.
        flag = False
        # look through every bag
        for bag in my_luggage:
            # print(f'looking at {bag}')
            if bag[0] in container_list:
                # print('Already in my list, resetting')
                continue
            # look at what this bag holds
            for inside in bag[1]:
                # check if it matches our target list
                # print(inside)
                if any(str in inside[1] for str in container_list):
                    # print('found it')
                    # if found, add this bag to our search target list, as long as it's unique
                    if bag[0] not in container_list:
                        container_list.append(bag[0])
                        flag = True

    return len(container_list)-1


def count_packed(target, my_luggage):

    my_count = 1
    # find the index of the target color bag
    for i in range(len(my_luggage)):
        if my_luggage[i][0] == target:
            break

    print(f'{target} has {my_luggage[i][1]}')

    if my_luggage[i][1]:
        print(f'{my_luggage[i][0]} has subs')
        for subs in my_luggage[i][1]:
            print(f'rec call for {subs}')
            this_count = count_packed(subs[1], my_luggage)
            mult = int(subs[0])
            print(f'I think I found {mult}')
            this_count = this_count * mult
            print(f'After call for {subs} count is {this_count}')
            my_count += this_count


    print(f'after {target} count, returning {my_count}')
    return my_count


def main():
    raw_data = read_file('day_07.dat', 'l')
    # print(raw_data)
    luggage = []
    for line in raw_data:
        luggage = pack_luggage(line, luggage)

    print(count_luggage('shiny gold', luggage))

    # count is always 1 high, correct by subbing one
    print(int(count_packed('shiny gold', luggage)) - 1)

if __name__ == '__main__':
    print('Running day 07 directly')
    main()
