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


# def create_category(category):
#     max_id = CATEGORIES[-1]["id"]
#     #This gets the id value of the last category on the list

#     #This adds 1 to whatever the index number is
#     new_id = max_id + 1

#     #This adds an id property to the category dictionary
#     category["id"] = new_id

#     #This adds the category dictionary to the list
#     CATEGORIES.append(category)

#     #Returns the dictionary with id property added
#     return category

#     #build a sql statement above

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

def get_single_category():
    with sqlite3.connect('./rare.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM categories c
        """)
        categories = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            category = Category(**row)
            categories.append(category.__dict__)
    return json.dumps(categories)