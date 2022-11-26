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

    def is_valid(self):
        members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
        for key in members:
            if self.__dict__[key] == 'Null' and key != 'cid':
                return False
        return True

    def strict_valid(self):


def make_id(my_list):
    my_new_id = IdCard()

    # flatten my nested lists
    my_list = flatten(my_list)
    for data in my_list:
        # split to key:value pairs
        this_line = data.split(':')
        # assign key:value pairs
        my_new_id.__dict__[this_line[0]] = this_line[1]
    return my_new_id

def clean_data(my_raw_data):
    # we need an empty newline at the end of file to mark end
    # if last item isnt empty line, append it
    if my_raw_data[-1] != '':
        my_raw_data.append('')
    # make empty list for cleaned IDs
    my_clean_data = []

    this_id = []
    for line in my_raw_data:
        # when we hit the empty line, push the data to a cleaner list
        if line == '':
            # call make_id to return class IdCard
            new_id = make_id(this_id)
            my_clean_data.append(new_id)
            this_id.clear()
            continue
        this_id.append(line.split(' '))

    return my_clean_data


def main():
    raw_data = read_file('day_04.dat')
    print(raw_data)
    id_list = clean_data(raw_data)
    valid_count = 0
    for person in id_list:
        print(person)
        if person.is_valid():
            valid_count += 1
        print(f'Valid: {person.is_valid()}\n')
    print(f'Total valid: {valid_count}')


# internal run testing
if __name__ == '__main__':
    main()

