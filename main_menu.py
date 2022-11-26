import importlib
import os
import sys

if __name__ == '__main__':
    sys.path.append('/home/mendoncapatrick/PycharmProjects/advent2020/code')
    sys.path.append('/home/mendoncapatrick/PycharmProjects/advent2020/dat')
    # print(sys.path)

    # import list of py files from code/ subdir
    options = os.listdir('code/')
    # remove support scripts from options
    options.remove('file_io.py')
    options.remove('__pycache__')
    options.remove('__init__.py')

    # print(options)
    # items on menu for print and indexing
    menu_size = len(options)

    # strip .py for import statements
    for i in range(menu_size):
        this_file = options[i]
        this_file = this_file.split('.')
        # print(this_file)
        options[i] = this_file[0]
    del this_file

    # loop menu until exit
    while True:

        # print menu
        print('Script Options:')
        for line in options:
            print(f'\t{options.index(line)+1}. {line}')
        print('\tx: Exit')

        # input
        menu_choice = input(':')
        if menu_choice == 'x': break

        # check menu input, and attempt to run script
        try:
            menu_choice = int(menu_choice) - 1
        except:
            print('Invalid Menu Choice!')
            continue

        if 0 <= menu_choice < menu_size:
            try:
                file_name = 'code.' + options[menu_choice]
                print(f'Trying to run {file_name}...')
                my_module = importlib.import_module(file_name)
            except:
                print('I had an error trying to run the file')
                continue

            print('Imported Module...\n\n')
            my_module.main()
            print('\n\n')

        else:
            print('Invalid Menu Choice!')
            continue