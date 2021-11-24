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
        """)
        categories = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            category = Category(**row)
            categories.append(category.__dict__)
    return json.dumps(categories)

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