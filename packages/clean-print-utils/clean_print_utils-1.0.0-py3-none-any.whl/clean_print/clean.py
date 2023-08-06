def sline_print(arg):
    print('')
    print('\033[K', end='')
    print(f'{arg}', end='\r')
