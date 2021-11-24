import sqlite3
import json
import categories

from models import Category

CATEGORIES = [
    {
        "id": 1,
        "label": "flowers"
    },
    {
        "id": 2,
        "label": "cookies"
    },
    {
        "id": 3,
        "label": "hair"
    }
]

def get_all_categories():
    with sqlite3.connect('./rare.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            c.id,
            c.label
    FROM Categories c
    """)
    categories = []
    dataset = db_cursor.fetchall()
    for row in dataset:
        category = Category(**row)
        categories.append(category.__dict__)
    return json.dumps(categories)

def get_single_category(id):
    with sqlite3.connect('./rare.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM categories c
        WHERE c.id = ?
        """, (id, ))
        row = db_cursor.fetchone()
        category = Category(**row) if row else None
    return json.dumps(category.__dict__) if category else ""
    ##  If the row doesn't return anything I want an empty string(falsey);Ternary; Helps me get a 404 code; dictionary is (truthy)
##Line 52 is where it takes the information & makes it readable like when we retrieve an APIs information

def create_category(post_data):
    new_category = Category(**post_data)
    with sqlite3.connect('./rare.db') as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
            INSERT INTO Categories (
                id, label
            ) VALUES ( ?, ?);
        """, (
            new_category.id, new_category.label
        ))
        
        id = db_cursor.lastrowid
        new_category.id = id
    return new_category

def delete_category(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute ("""
        DELETE FROM category
        WHERE id =?
        """, (id, ))

#Update Category

def update_category(id, new_category):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Categories
            SET
                label = ?
        WHERE id = ?
        """, (new_category['label'], id,))

        rows_affected = db_cursor.rowcount
    
    if rows_affected == 0:
        return False
    else:
        return True