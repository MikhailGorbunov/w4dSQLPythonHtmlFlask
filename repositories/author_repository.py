from db.run_sql import run_sql

from models.author import Author
from models.book import Book 

def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql) # why do we use results
    for row in results:
        author = Author (row['f_name'], row['l_name'], row['id'])
        authors.append(author)
    return authors

def select(id):
    sql = "SELECT * FROM author WHERE id=%s"
    values = [id] # this takes the list of id 
    result = run_sql(sql, values)[0] # results show only sql and values for position 0 in the list of id.

    if result is not None:
        author = Author(result['f_name'], result['l_name'], result['id'])
    return author 