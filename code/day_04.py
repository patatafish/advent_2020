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

    def is_valid(self, strict=True):

        members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
        # first check, see if any members are Null, ignoring CID
        for key in members:
            if self.__dict__[key] == 'Null' and key != 'cid':
                return False
        # if not a strict check, return valid status after checks
        if not strict:
            return True
        # if is a strict check, procede with further validation
        # we pass through each check immediately returning false
        # if any check fails. After all checks passed we return
        # true valid status
        else:
            # BYR valid range 1920-2002
            if int(self.byr) > 2002 or int(self.byr) < 1920:
                print('byr')
                return False
            # IYR valid range 2010-2020
            if int(self.iyr) > 2020 or int(self.iyr) < 2010:
                print('iyr')
                return False
            # EYR valid range 2020-2030
            if int(self.eyr) > 2030 or int(self.eyr) < 2020:
                print('eyr')
                return False
            # HGT valid range 150-193 cm, 59-76 in
            number = int(self.hgt[:-2])
            unit = self.hgt[-2:]
            if unit != 'cm' and unit != 'in':
                print('unit')
                return False
            if unit == 'cm' and (number > 193 or number < 150):
                print('cm')
                return False
            if unit == 'in' and (number > 76 or number < 59):
                print('in')
                return False
            # HCL must be valid HEX, #(6 digits)
            if self.hcl[0] != '#' or len(self.hcl) != 7:
                print('hcl format')
                return False
            if not all(char in '0123456789abcdefABCDEF' for char in self.hcl[1:]):
                print('hcl hex')
                return False
            # ECL one of (amb, blu, brn, gry, grn, hzl, oth)
            if self.ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] or len(self.ecl) > 3:
                print('ecl')
                return False
            # PID 9 digit number including leading zero
            if not all(char in '0123456789' for char in self.pid) or len(self.pid) != 9:
                print('pid')
                return False
            # CID not checked
            return True

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
    strict_count = 0
    for person in id_list:
        print(person)
        check = person.is_valid(strict=False)
        strict_check = person.is_valid(strict=True)
        if check:
            valid_count += 1
        print(f'Valid: {check}')
        if strict_check:
            strict_count += 1
        print(f'Strict: {strict_check}\n')
        # if check and strict_check:
            # input()
    print(f'Total valid: {valid_count}')
    print(f'Total strict: {strict_count}')


# internal run testing
if __name__ == '__main__':
    main()

