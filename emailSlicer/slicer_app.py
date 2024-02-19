# Slicer will return: username, domain, extension
def app_slicer():

    usr_input = input('Enter your email address:')

    (username, domain) = usr_input.split('@')
    (domain, extension) = usr_input.split('.')
    print(f'\n Username: {username}')
    print(f'Domain: {domain}')
    print(f'Extension: {extension} \n ----------------------------------- \n')


while True:
    print(' Email Slicing App \n Type e to exit the app.')
    prg = input('Press any other key to continue: ')
    print('-----------------------------------')
    if prg == 'e':
        print('Exiting the app')
        exit()
    elif prg != 'e':
        app_slicer()
