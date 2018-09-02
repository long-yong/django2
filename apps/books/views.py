"""   views.py
"""
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from applib.yong.comfunc import *
from apps.books.models import *

# Author

def author_id(name):
    if Author.objects.filter(name=name).exists(): pass
    else: Author.objects.create(name=name)
    author = Author.objects.get(name=name)
    return author.id

# Book many-one Author

def books_add(title, name):
    id = author_id(name)
    if Book.objects.filter(title=title, author=Author.objects.get(id=id)).exists(): return
    Book.objects.create(title=title, author=Author.objects.get(id=id))

def book_id(title, name):
    books_add(title, name)
    id = author_id(name)
    book = Book.objects.get(title=title, author=Author.objects.get(id=id))
    return book.id

def book_dels(title):
    if Book.objects.filter(title=title).exists():
        Book.objects.filter(title=title).delete()

def book_qry():
    showQry(Book.objects.filter(author__name="yong"))
    showQry(Book.objects.filter(author__name__startswith="y"))

# Publisher many-many Book

def publisher_id(name):
    if Publisher.objects.filter(name=name).exists(): pass
    else: Publisher.objects.create(name=name)
    publisher = Publisher.objects.get(name=name)
    return publisher.id

def many_add_many(pid, bid):
    book = Book.objects.get(id=bid)
    publisher = Publisher.objects.get(id=pid)
    if book not in publisher.books.all():
        publisher.books.add(book)

def publisher_add_book(pname, title, name):
    pid = publisher_id(pname)
    publisher = Publisher.objects.get(id=pid)
    bid = book_id(title, name)
    book = Book.objects.get(id=bid)
    if book not in publisher.books.all():
        publisher.books.add(book)

def show_publisher_book():
    print("\n----- many to many -----")
    for p in Publisher.objects.all():
        for b in p.books.all():
            print(p.id, b.id)

# routes

def index(request):
    checkPostOnce(request)
    context = {"authors": Author.objects.all()}
    return render(request, "books/index.html", context)

def index_post(request):
    addPostOnce(request)
    books_add('book_1', 'yong')
    publisher_add_book('lisa', 'book_9', 'zhang')
    book_dels("Little Women")

    showCls(Author, ['id', 'name'])
    showCls(Book, ['id', 'title'])
    show_publisher_book()

    return redirect("/books/index")




