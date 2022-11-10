import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository

import repositories.book_repository as book_repository

author_repository.delete_all()
book_repository.delete_all()


author1 = Author ("m1")
