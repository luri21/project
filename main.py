def print_username(name):
    print("Ваше ім'я:", name)
username = input("Введіть ваше ім'я: ")
print_username(username)
def print_multiplication_table(number):
    print(f"Таблиця множення на {number}:")
    for i in range(1, 11):
        print(f"{i} * {number} = {i * number}")
num = int(input("Введіть число: "))
print_multiplication_table(num)
def print_numbers(start, end):
    print(f"Числа у діапазоні від {start} до {end}:")
    for num in range(start, end + 1):
        print(num)
start_num = int(input("Введіть початкове число: "))
end_num = int(input("Введіть кінцеве число: "))
print_numbers(start_num, end_num)
def calculate_sum(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return total

start_num = int(input("Введіть початкове число: "))
end_num = int(input("Введіть кінцеве число: "))
result = calculate_sum(start_num, end_num)
print("Сума чисел:", result)
def print_day_of_week(day_number):
    days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
    if 1 <= day_number <= 7:
        print("Назва дня тижня:", days[day_number - 1])
    else:
        print("Неправильний номер дня тижня")

day_num = int(input("Введіть номер дня тижня (1-7): "))
print_day_of_week(day_num)
def print_month_name(month_number):
    months = ["Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень", "Липень", "Серпень", "Вересень",]
