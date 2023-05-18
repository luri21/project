import datetime

def log_event(event):
    timestamp = datetime.datetime.now()
    print(f"[{timestamp}] {event}")

def register_account():
    username = input("Введіть ім'я користувача: ")
    password = input("Введіть пароль: ")


    log_event(f"Зареєстровано новий аккаунт: {username}")



def login():
    username = input("Введіть ім'я користувача: ")
    password = input("Введіть пароль: ")



    if is_valid_credentials(username, password):
        log_event(f"Увійшов на аккаунт: {username}")
        print("Успішний вхід в аккаунт")
    else:
        log_event(f"Невдала спроба входу на аккаунт: {username}")
        print("Неправильне ім'я користувача або пароль")

def is_valid_credentials(username, password):

    return False

while True:
    print("1. Вхід в аккаунт")
    print("2. Реєстрація аккаунта")
    print("3. Вийти")

    choice = input("Виберіть опцію: ")

    if choice == "1":
        login()
    elif choice == "2":
        register_account()
    elif choice == "3":
        break
    else:
        print("Неправильний вибір")