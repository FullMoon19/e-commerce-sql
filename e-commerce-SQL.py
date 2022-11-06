# fill in the database with fake data created with the Faker library

import sqlite3
import os
from faker import Faker
from random import randint

# create a connection to the database
conn = sqlite3.connect('e-commerce-SQL.db')
# create a cursor
c = conn.cursor()

# create a Faker instance
fake = Faker()

# create a list of genres
categories = ['Femme', 'Homme', 'Enfant', 'Bébé', ]

# insert the genres in the database
for categorie in categories:
    c.execute("INSERT INTO Categorie (name) VALUES (?)", (categorie,))
    conn.commit()

# insert the users in the database
for i in range(100):
    c.execute("INSERT INTO Users (firstName, lastName, email, pwd) VALUES (?, ?, ?, , ?)", (fake.firstName(), fake.lastName(), fake.email(), fake.pwd()))
    conn.commit()

# insert the address in the database
for i in range(100):
    c.execute("INSERT INTO Address (userID, country, city, postCode) VALUES (?, ?, ?, ?)", (i+1, fake.country(), fake.city(), fake.postcode()))
    conn.commit()

# insert the products in the database
for i in range(100):
    c.execute("INSERT INTO Product (name, id_genre, description, price, image, stock) VALUES (?, ?, ?, ?, ?, ?)", (fake.company(), randint(1, 18), fake.text(), fake.pyfloat(left_digits=2, right_digits=2, positive=True), fake.image_url(), randint(1, 100)))
    conn.commit()

# # insert the commands in the database
# for i in range(100):
#     c.execute("INSERT INTO Command (id_user, total) VALUES (?, ?)", (i+1, fake.pyfloat(left_digits=2, right_digits=2, positive=True)))
#     conn.commit()

# # insert the command lines in the database
# for i in range(100):
#     c.execute("INSERT INTO Command_line (id_command, id_product) VALUES (?, ?)", (i+1, randint(1, 100)))
#     conn.commit()

# # insert the carts in the database
# for i in range(100):
#     c.execute("INSERT INTO Cart (id_user, cart_date, total) VALUES (?, ?, ?)", (i+1, fake.date(), fake.pyfloat(left_digits=2, right_digits=2, positive=True)))
#     conn.commit()

# # insert the cart_temp in the database
# for i in range(100):
#     c.execute("INSERT INTO Cart_temp (id_cart, id_product) VALUES (?, ?)", (i+1, randint(1, 100)))
#     conn.commit()

# close the connection
conn.close()