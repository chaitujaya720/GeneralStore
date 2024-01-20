import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()


cur.execute("INSERT INTO location (name, description) VALUES (?, ?)",
            ('Perimeter', 'This is the 1st location')
            )

cur.execute("INSERT INTO location (name, description) VALUES (?, ?)",
            ('Center', 'This is the 2nd location')
            )

cur.execute("INSERT INTO department (name, location_id, description) VALUES (?, ?, ?)",
            ('Bakery', 1, 'Deals with bakery products')
            )

cur.execute("INSERT INTO department (name, location_id, description) VALUES (?, ?, ?)",
            ('Dairy', '2', 'Deals with dairy products')
            )

cur.execute("INSERT INTO department (name, location_id, description) VALUES (?, ?, ?)",
            ('Frozen', '2', 'Deals with frozen products')
            )

cur.execute("INSERT INTO category (name, department_id, description) VALUES (?, ?, ?)",
            ('Bakery Bread', 1, '')
            )

cur.execute("INSERT INTO category (name, department_id, description) VALUES (?, ?, ?)",
            ('In Store Bakery', 1, '')
            )

cur.execute("INSERT INTO category (name, department_id, description) VALUES (?, ?, ?)",
            ('Cheese', 2, '')
            )

cur.execute("INSERT INTO category (name, department_id, description) VALUES (?, ?, ?)",
            ('Cream or Creamer', 2, '')
            )

cur.execute("INSERT INTO category (name, department_id, description) VALUES (?, ?, ?)",
            ('Frozen Bake', 3, '')
            )

cur.execute("INSERT INTO sub_category (name, category_id, description) VALUES (?, ?, ?)",
            ('Bagels', 1, '')
            )

cur.execute("INSERT INTO sub_category (name, category_id, description) VALUES (?, ?, ?)",
            ('Baking or Breading Products', 1, '')
            )

cur.execute("INSERT INTO sub_category (name, category_id, description) VALUES (?, ?, ?)",
            ('English Muffins or Biscuits', 1, '')
            )

cur.execute("INSERT INTO sub_category (name, category_id, description) VALUES (?, ?, ?)",
            ('Flatbreads', 1, '')
            )

cur.execute("INSERT INTO sub_category (name, category_id, description) VALUES (?, ?, ?)",
            ('Breakfast Cake or Sweet Roll', 2, '')
            )

cur.execute("INSERT INTO sub_category (name, category_id, description) VALUES (?, ?, ?)",
            ('Cakes', 2, '')
            )

cur.execute("INSERT INTO sub_category (name, category_id, description) VALUES (?, ?, ?)",
            ('Pies', 2, '')
            )

cur.execute("INSERT INTO sub_category (name, category_id, description) VALUES (?, ?, ?)",
            ('Seasonal', 2, '')
            )

cur.execute("INSERT INTO sub_category (name, category_id, description) VALUES (?, ?, ?)",
            ('Cheese Sauce', 3, '')
            )

cur.execute("INSERT INTO sub_category (name, category_id, description) VALUES (?, ?, ?)",
            ('Specialty Cheese', 3, '')
            )

cur.execute("INSERT INTO sub_category (name, category_id, description) VALUES (?, ?, ?)",
            ('Dairy Alternative Creamer', 4, '')
            )
cur.execute("INSERT INTO sub_category (name, category_id, description) VALUES (?, ?, ?)",
            ('Bread or Dough Products Frozen', 5, '')
            )

cur.execute("INSERT INTO sub_category (name, category_id, description) VALUES (?, ?, ?)",
            ('Breakfast Cake or Sweet Roll Frozen', 4, '')
            )

connection.commit()
connection.close()

# SELECT loc.NAME,
#        dep.NAME,
#        cat.NAME,
#        sub.NAME
# FROM   sub_category sub
#        JOIN category cat
#          ON sub.category_id = cat.id
#        JOIN department dep
#          ON cat.department_id = dep.id
#        JOIN location loc
#          ON dep.location_id = loc.id;
