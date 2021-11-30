import sqlite3
import json
from models import Post, Category

POSTS = [
    
]

def get_all_posts():
    # Open a connection to the database
    with sqlite3.connect("./rare.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM posts p
        """)

        # Initialize an empty list to hold all post representations
        posts = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        for row in dataset:

            # Create a post instance from the current row
            post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row['publication_date'], row['image_url'], row['content'], row['approved'])

            # Add the dictionary representation of the post to the list
            posts.append(post.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(posts)


def get_single_post(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM posts p
        WHERE p.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        post = Post(data['id'], data['user_id'], data['category_id'], data['title'],
                            data['publication_date'], data['image_url'],
                            data['content'], data['approved'])

    return json.dumps(post.__dict__)


def create_post(new_post):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Post
            ( user_id, category_id, title, publication_date, image_url, content, approved )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_post['user_id'], new_post['category_id'],
              new_post['title'], new_post['publication_date'],
              new_post['image_url'], new_post['content'], new_post['approved'] ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_post['id'] = id

def get_posts_by_category_id(category_id):

    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

#This is the SQL query to get the info I want
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            c.label
        FROM Posts p
        JOIN Categories c
        ON c.id = p.category_id
        WHERE p.category_id = ?
        """, (category_id,))

        
        dataset = db_cursor.fetchall()
        posts = []
        for row in dataset:
        #create a post from the current row
            post = Post(row['id'], row['user_id'], row['category_id'],
                        row['title'], row['publication_date'],
                        row['image_url'], row['content'], row['approved'])
            ##now I'm creating a Category instance from the current row
            category = Category(row['category_id'], row['label'])
            ##add the dictionary representation of the category to the post
            post.category = category.__dict__

        ##Add the dictionary representation of the post to the list
            posts.append(post.__dict__)


        return json.dumps(posts)
