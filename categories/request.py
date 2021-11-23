import sqlite3
import json
import categories

from models import Category


def create_category(category):
    max_id = CATEGORIES[-1]["id"]
    #This gets the id value of the last category on the list

    #This adds 1 to whatever the index number is
    new_id = max_id + 1

    #This adds an id property to the category dictionary
    category["id"] = new_id

    #This adds the category dictionary to the list
    CATEGORIES.append(category)

    #Returns the dictionary with id property added
    return category

    #build a sql statement above