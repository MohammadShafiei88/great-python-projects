def password_checker(password: str):
    with open('passwords.text', 'r') as file:
        common_passwords: list[str] = file.read().splitlines()

    for i,common_password in enumerate(common_passwords, start=1):
        if password == common_password:
            print(f'password: {password} is the {i}th common_password ❌')
            return
    print(f'password: {password} is unique ✅')


def main():
    user_password: str = input('Enter a password: ')
    if user_password == '':
        print('Please enter a valid password')
    else:
        password_checker(password=user_password)


if __name__ == '__main__':
    main()










