import sqlite3


conn = sqlite3.connect('products.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    price REAL,
                    quantity INTEGER
                )''')

def add_product(name, price, quantity):

    cursor.execute("INSERT INTO Products (name, price, quantity) VALUES (?, ?, ?)", (name, price, quantity))
    conn.commit()
    print("Товар додано успішно.")

def delete_product(product_id):

    cursor.execute("DELETE FROM Products WHERE id = ?", (product_id,))
    conn.commit()
    print("Товар видалено успішно.")

def edit_product(product_id, new_name, new_price, new_quantity):

    cursor.execute("UPDATE Products SET name = ?, price = ?, quantity = ? WHERE id = ?", (new_name, new_price, new_quantity, product_id))
    conn.commit()
    print("Товар відредаговано успішно.")

def view_products():

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    if len(products) > 0:
        for product in products:
            print(f"ID: {product[0]}, Назва: {product[1]}, Ціна: {product[2]}, Кількість: {product[3]}")
    else:
        print("Список товарів порожній.")

while True:
    print("\nМеню:")
    print("1. Додати товар")
    print("2. Видалити товар")
    print("3. Редагувати товар")
    print("4. Переглянути список товарів")
    print("5. Вийти з програми")

    choice = input("Виберіть дію (1-5): ")

    if choice == '1':
        name = input("Введіть назву товару: ")
        price = float(input("Введіть ціну товару: "))
        quantity = int(input("Введіть кількість товару: "))
        add_product(name, price, quantity)
    elif choice == '2':
        product_id = int(input("Введіть ID товару: "))
        delete_product(product_id)
    elif choice == '3':
        product_id = int(input("Введіть ID товару: "))
        new_name = input("Введіть нову назву товару: ")
        new_price = float(input("Введіть нову ціну товару: "))
        new_quantity = int(input("Введіть нову кількість товару: "))
        edit_product(product_id, new_name, new_price, new_quantity)
    elif choice == '4':
        view_products()
    elif choice == '5':
        break
    else:
        print("Неправильнийkpbvb  вибір. Спробуйте ще раз.")

import sqlite3

