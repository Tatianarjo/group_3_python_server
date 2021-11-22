import sqlite3
import json
import users

from models import User

USERS = [
    {
        "id": 1,
        "first_name": "Nancy",
        "last_name": "Drew",
        "email":  "nancy@nancy.com",
        "bio":"hello world",
        "username": "nancy",
        "password": 123

    }
]


def create_user(post_data):
    new_user = User(**post_data)

    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor() 
        db_cursor.execute("""
            INSERT INTO Users (
                id, first_name, last_name, email,
                bio, username, password, profile_image_url,
                created_on, active
            ) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, ( 
            new_user.id, new_user.first_name, new_user.last_name, new_user.email,
            new_user.bio, new_user.username, new_user.password, new_user.profile_image_url,
            new_user.created_on, new_user.active
        ))

        id = db_cursor.lastrowid
        new_user.id = id
    
    return new_user


def login_user(user_data):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor() 
        db_cursor.execute("""
            sElEcT * fRoM Users u
            where
            u.username = ?
            and 
            u.password = ?;
        """, (user_data['username'], user_data['password']))

        result = db_cursor.fetchone()

        if not result:
            return None
        else:
            return User(**result)

#Function with a single parameter
def get_single_user(id):
    with sqlite3.connect('./rare.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
        FROM users u
        WHERE u.id = ?
        """, ( id, ))
        data = db_cursor.fetchone()
        user = User(**data)
        return json.dumps(user.__dict__)
   
    
def get_all_users():
    with sqlite3.connect('./rare.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
        FROM users u
        """)
        users = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            user = User(**row)
            users.append(user.__dict__)
    return json.dumps(users)









