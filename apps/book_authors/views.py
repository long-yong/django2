"""   views.py
"""
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from applib.yong.comfunc import *
from apps.book_authors.models import *

# class Book(models.Model):
#     name = models.CharField(max_length=255)
#     desc = models.TextField(max_length=1000)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
# class Author(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     books = models.ManyToManyField(Book, related_name="authors")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

def show_authors_books():
    print("\n----- author book -----")
    for a in Author.objects.all():
        for b in a.books.all():
            print(a.id, b.id)
    print(' ')

def show_all():
    showCls(Book, ['id', 'name'])
    showCls(Author, ['id', 'first_name'])
    show_authors_books()

# Book

def book_add(name, desc=''):
    if Book.objects.filter(name=name).exists(): pass
    else: Book.objects.create(name=name, desc=desc)
    get = Book.objects.get(name=name)
    return get.id

def book_id(name,desc=''):
    return book_add(name, desc)

def book_update(id, name):
    get = Book.objects.get(id=id)
    get.name = name
    get.save()

# Author

def author_add(first_name, last_name="", email=""):
    if Author.objects.filter(first_name=first_name, last_name=last_name).exists(): pass
    else: Author.objects.create(first_name=first_name, last_name=last_name, email=email)
    get = Author.objects.get(first_name=first_name, last_name=last_name)
    return get.id

def author_id(first_name, last_name=""):
    return author_add(first_name, last_name)

def author_update(id, name):
    get = Author.objects.get(id=id)
    get.first_name = name
    get.save()

# Book many-many Author

def assign_book_author(bname, first_name, last_name=''):
    aid = author_id(first_name, last_name)
    author = Author.objects.get(id=aid)
    bid = book_id(bname)
    book = Book.objects.get(id=bid)
    if book not in author.books.all():
        author.books.add(book)

def assign_author_book(aid, bid):
    author = Author.objects.get(id=aid)
    book = Book.objects.get(id=bid)
    if book not in author.books.all():
        author.books.add(book)

# routes

def index(request):
    checkPostOnce(request)
    context = {}
    return render(request, "book_authors/index.html")

def index_post(request):
    addPostOnce(request)

    book_add('C sharp')
    book_add('Java')
    book_add('Python')
    book_add('PHP')
    book_add('Ruby')

    author_add('Mike')
    author_add('Speros')
    author_add('John')
    author_add('Jadee')
    author_add('Jay')

    book_update(5, "C#")
    author_update(5, 'Ketul')

    for i in range(1, 3): assign_author_book(1, i)
    for i in range(1, 4): assign_author_book(2, i)
    for i in range(1, 5): assign_author_book(3, i)
    for i in range(1, 6): assign_author_book(4, i)

    show_all()

    return redirect("/book_authors/index")



# For the 3rd book, retrieve all the authors
# For the 3rd book, remove the first author
# For the 2nd book, add the 5th author as one of the authors
# Find all the books that the 3rd author is part of
# Find all the books that the 2nd author is part of




