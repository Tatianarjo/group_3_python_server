import sqlite3
import json
from models import Comment

def get_all_comments():
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id,
            c.author_id,
            c.content
        FROM Comments c
        """)
        comments = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            comment = Comment(**row)
            comments.append(comment.__dict__)
        return json.dumps(comments)

def get_single_comment(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id,
            c.author_id,
            c.content
        FROM Comments c
        WHERE c.id = ?
        """, (id, ))
        row = db_cursor.fetchone()
        comment = Comment(**row)
    return json.dumps(comment.__dict__)