def routine_1():
    print('Routine 1 done.')


def routine_2():
    sub_routine_1()
    sub_routine_2()
    print('Routine 2 done.')


def sub_routine_1():
    print('Sub-routine 1 done.')


def sub_routine_2():
    print('Sub-routine 2 done.')


def main():
    routine_1()
    routine_2()
    print('This is the end of the program.')


if __name__ == '__main__':
    main()