import json

def load_books():
    print("Loading all books...")

load_books()

def search_book(title):
    print(f"Searching for book: {title}")

def remove_book(title):
    print(f"Removing book: {title}")
    search_book("Clean Code")
remove_book("Clean Code")