

import sqlite3

conn = sqlite3.connect('store.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
''')
conn.commit()




def add_product(name, price):
    cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
    conn.commit()
    print('Товар успішно додано.')

def delete_product(product_id):
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    print('Товар успішно видалено.')


def edit_product(product_id, new_name, new_price):
    cursor.execute('UPDATE products SET name = ?, price = ? WHERE id = ?', (new_name, new_price, product_id))
    conn.commit()
    print('Товар успішно відредаговано.')

def view_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    print('Товари:')
    for product in products:
        print(f'ID: {product[0]}, Назва: {product[1]}, Ціна: {product[2]}')


print('Ласкаво просимо до адміністративної сторони магазину!')

while True:
    def login():
        password = input('Введіть пароль для входу: ')
        if password == '123':
            print('Успішний вхід!')
            return True
        else:
            print('Невірний пароль.')
            return False


    print('Ласкаво просимо до адміністративної сторони магазину!')


    if not login():
            continue
    print('\nМеню:')
    print('1. Переглянути товари')
    print('2. Додати товар')
    print('3. Видалити товар')
    print('4. Редагувати товар')
    print('5. Вийти')
    print('6. ?')
    choice = input('Виберіть дію: ')




    if choice == '1':
        view_products()
    elif choice == '2':
        name = input('Введіть назву товару: ')
        price = float(input('Введіть ціну товару: '))
        add_product(name, price)
    elif choice == '3':
        product_id = input('Введіть ID товару, який потрібно видалити: ')
        delete_product(product_id)
    elif choice == '4':
        product_id = input('Введіть ID товару, який потрібно редагувати: ')
        new_name = input('Введіть нову назву товару: ')
        new_price = float(input('Введіть нову ціну товару: '))
        edit_product(product_id, new_name, new_price)
    elif choice == '5':
        print('До побачення!')
        break
    elif choice == '6':
        product_id = input('Введіть ID товару, який потрібно редагувати: ')
        new_name = input('Введіть нову назву товару: ')
        new_price = float(input('Введіть нову ціну товару: '))
        edit_product(product_id, new_name, new_price)
    else:
        print('Невірний вибір. Спробуйте ще раз.')

cursor.close()
conn.close()








