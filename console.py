import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository

import repositories.book_repository as book_repository

author_repository.delete_all()
book_repository.delete_all()


author1 = Author ("f1","l2")
author2 = Author ("f2", "l2")
author_repository.save(author1)
author_repository.save(author2)
author_repository.select_all()
book1 = Book (a1,b1, author1)
book2 = Book (a2,b2, author2)
book_repository.save(book1)
book_repository.save(book2)
# book_repository.select_all()
pdb.set_trace()
