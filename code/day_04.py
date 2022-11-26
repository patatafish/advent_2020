import file_io

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
               f'ECL:{sefl.ecl}\nPID:{self.pid}\nCID:{self.cid}'


def main():
    raw_data = file_io.read_file('test.dat', 'l')
    print(raw_data)






# internal run testing
if __name__ == '__main__':
    main()

