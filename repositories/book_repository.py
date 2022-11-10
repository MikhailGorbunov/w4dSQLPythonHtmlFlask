from db.run_sql import run_sql

from models.author import Author
from models.book import Book 

import repositories.author_repository as author_repository


def select_all():
    books = []
    sql = "SELECT * FROM author"
    results = run_sql(sql)
    
    for row in results:
        author = author_repository.select(row['user_id']) # this comes from select function for author can be seen in postico
        book = Book(row['name'], row['title'], author, row['id'])
        books.append(book)
    return books

def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = author_repository.select(result['author_id'])
        book = Book(result['name'],result['title'], author, result['id'])
    return book

def delete_all():
    sql = "DELETE  FROM books "
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM books WHERE id=%s"
    values = [id]
    run_sql(sql, values)