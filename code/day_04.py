from shared_use import flatten, read_file

# create a class for the ID cards
class IdCard:
    def __init__(self, byr='Null', iyr='Null', eyr='Null', hgt='Null', hcl='Null', ecl='Null', pid='Null', cid='Null'):
        """
        byr (Birth Year)
        iyr (Issue Year)
        eyr (Expiration Year)
        hgt (Height)
        hcl (Hair Color)
        ecl (Eye Color)
        pid (Passport ID)
        cid (Country ID)"""
        # pass values to variables, leave as Null if no data passed
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    def __str__(self):
        return f'BYR:{self.byr}\nIYR:{self.iyr}\nEYR:{self.eyr}\nHGT:{self.hgt}\nHCL:{self.hcl}\n' \
               f'ECL:{self.ecl}\nPID:{self.pid}\nCID:{self.cid}'

def make_id(my_list):
    my_new_id = IdCard()

    # flatten my nested lists
    my_list = flatten(my_list)
    print(f'flat:{my_list}')

    return my_new_id

def clean_data(my_raw_data):
    # make empty list for cleaned IDs
    my_clean_data = []

    this_id = []
    for line in my_raw_data:
        # when we hit the empty line, push the data to a cleaner list
        if line == '':
            print('EOF')
            # call make_id to return class IdCard
            new_id = make_id(this_id)
            # print(new_id)
            my_clean_data.append(new_id)
            this_id.clear()
            continue
        this_id.append(line.split(' '))
        # print(f'this id:{this_id}')


def main():
    raw_data = read_file('test.dat')
    print(raw_data)
    id_list = clean_data(raw_data)




# internal run testing
if __name__ == '__main__':
    main()

