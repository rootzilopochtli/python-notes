# 7. Dictionaries
book = {
    'title' : 'atomic habits',
    'author': "James Clear",
    'isbn'  : '234-23-2-523',
    "page_count" : 234
}
# access
book_title = book['title']
book['title'] = '2020 what went wrong'
#print(book)
# Keys
keys = book.keys()
#print(keys)
# list of dict
personalities = [{
    "name" : "chancelor",
    "age" : 18
},{
    "name" : "ronald",
    "age" : 22
}]
#print(personalities)

# Exercise
# A bag dictionary:
# book, stationary, size, color
"""
bag = [{
    "book_id" : "0",
    "title" : "Mountains of madness",
    "stationary" : "AB25",
    "size" : "medium",
    "color" : "cherry"
},{
    "book_id" : "1",
    "title" : "The Crow",
    "stationary" : "AP05",
    "size" : "small",
    "color" : "black"
}]
print(bag)
"""
bag = {
    "books" : [{
    'title' : 'atomic habits',
    'author': "James Clear",
    'isbn'  : '234-23-2-523',
    "page_count" : 234
    },{
    'title' : 'you only live once',
    'author': "Nobody",
    'isbn'  : '234-23-2-523',
    "page_count" : 2234
    }],
    "stationaries": [{
        "name": "pencil",
        "quantity": 10
    },{
        "name": "ball pen",
        "quantity": 2
    }],
    "size": 15,
    "color": "blue"
}
print(bag)
