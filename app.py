import json

def load_books():
    with open('books.json', 'r') as f:
        return json.load(f)

print("Library Books:", load_books())