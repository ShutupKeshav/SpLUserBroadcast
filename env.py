def read_vars() -> dict:
    while True:
        try:
            api_id: int = int(input('ENTER YOUR API_ID: '))
            break        
        except:
            print('API_ID must be Integers !')
    api_hash: str = input('ENTER YOUR API_HASH: ')
    session_string: str = input('ENTER YOUR STRING (Pyrogram): ')
    dic: dict = {
        'API_ID': api_id,
        'API_HASH': api_hash,
        'STRING_SESSION': session_string
    }
    return dic

def set_vars(dic: dict):
    with  open('vars.py', 'w+') as e:
        e.write(f'vars = {dic}')

def check_vars() -> bool:
    try:
        open('vars.py', 'r')
        return True
    except:
        return False

if check_vars():
    while True:
        yon: str = input('Vars already exists, You wanna overwrite ? (y/n): ')
        yon = yon.lower()
        if yon in ['y', 'n']:
            break
        else:
            print("Please Enter either 'y' or 'n' !")
    if yon == 'y':
        vars: dict = read_vars()
        set_vars(vars)
        print('ENV Vars have been set successfully !')
    else:
        print('Fine !')
else:
    vars: dict = read_vars()
    set_vars(vars)
    print('ENV Vars have been set successfully !')