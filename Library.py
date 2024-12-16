book_shelf=['Quran','Bible','gita']
while True:
    user_input=input()
    if user_input=="lend":
        print("Tell me the name of the book")
        name=input()

        if name in book_shelf:
            book_shelf.remove(name)
            print(book_shelf)
        else:
            print("the book is not available")
    elif user_input=='return':
        print("tell me the name of the book")
        book1=input()
    if book1 not in book_shelf:
        book_shelf.append(book1)
        print(book_shelf)
    else:
        print("the book is already there")