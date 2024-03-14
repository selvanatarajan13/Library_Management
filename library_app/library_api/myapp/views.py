from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .forms import AddBookForm,UpdateBookForm,AddMemberForm
from .models import *
import json

# Create your views here.

def header(request):
    return render(request, 'header.html',{})


# The below function handles incoming JSON data and saves it to the database.
@csrf_exempt
def save_json(request):
    if request.method == "POST":
        json_payload = json.loads(request.body)
        bookID = json_payload.get('bookID')
        title = json_payload.get('title')
        authors = json_payload.get('authors')
        average_rating = json_payload.get('average_rating')
        isbn = json_payload.get('isbn')
        isbn13 = json_payload.get('isbn13')
        language_code = json_payload.get('language_code')
        num_pages = json_payload.get('num_pages')
        ratings_count = json_payload.get('ratings_count')
        text_reviews_count = json_payload.get('text_reviews_count')
        publication_date = json_payload.get('publication_date')
        publisher = json_payload.get('publisher')

        book = Book.objects.create(
            bookID=bookID,
            title=title,
            authors=authors,
            average_rating=average_rating,
            isbn=isbn,
            isbn13=isbn13,
            language_code=language_code,
            num_pages=num_pages,
            ratings_count=ratings_count,
            text_reviews_count=text_reviews_count,
            publication_date=publication_date,
            publisher=publisher
        )
    return HttpResponse('JSON data was saved successfully!')

# CRUD Operations

# Fetch the Data
# Book data

def index(request):
    searched = ''
    tot_book = 0
    book_not = ''
    if 'search' in request.POST:
        searched = request.POST['search']
        Books_data = Book.objects.filter(title__contains = searched)

        if not Books_data:
            book_not = 'Book not available..'


        

    else:
        Books_data = Book.objects.all()
        tot_book = len(Books_data)
    
    context = {'data' : Books_data, 'tot_book':tot_book, 'book_not':book_not}

    return render(request, 'index.html', context)

# Member data

def member(request):

    searched = ''
    if 'search' in request.POST:
        searched = request.POST['search']
        member_data = members.objects.filter(member_name__icontains = searched)

        if not member_data:
            member_data = "Book not available"

    else:
        member_data = members.objects.all()
    
    context = {'data' : member_data}

    return render(request, 'members.html', context) 


# Create Operation
# Book

def Add_new_book(request):

    form = AddBookForm()
    if request.method == "POST":
        form = AddBookForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/')
        else:
            return redirect('/')
    context = {'form':form}

    return render(request,'Add_new_book.html',context=context)


# Add Member
def Add_new_member(request):

    form = AddMemberForm()

    if request.method == "POST":
        form = AddMemberForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/members')
        else:
            return redirect('/members')
    context = {'form':form}

    return render(request,'Add_new_member.html',context=context)

# Read operation
# single data fetch (Read)
    
def single_book_view(request,pk):
    if request.method == "GET":
        single_record = Book.objects.get(bookID=pk)
        context = {'data':single_record}

    return render(request, 'single_book_view.html',context=context)

def single_member_view(request,pk):
    if request.method == "GET":
        single_record = members.objects.get(reference_id=pk)
        context = {'data':single_record}
    return render(request, 'single_member_view.html',context=context)


# Update Operation
# Book
def update_book(request,pk):
    record = Book.objects.get(bookID=pk)
    form = UpdateBookForm(instance=record)
    if request.method == "POST":
        form = UpdateBookForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            return redirect('/')
        else:
            return redirect('/readers')
    context = {'form':form}

    return render(request,'Update_book.html',context=context)


# Delete Operation
# Book
def delete_book(request,pk):
    record = Book.objects.get(bookID = pk)
    record.delete()
    
    return redirect('/')

# Member
def delete_member(request,pk):
    record = members.objects.get(reference_id = pk)
    record.delete()
    
    return redirect('/')

def book_issue(request,pk):

    return render(request, 'book_issue.html')


# Transaction

def transaction(request):
    searched = ''
    tot_transaction = 0
    book_not = ''
    if 'search' in request.POST:
        searched = request.POST['search']
        transaction = Transaction.objects.filter(name__contains = searched)

        if not transaction:
            book_not = 'Book not available..'


        

    else:
        transaction = Transaction.objects.all()
        tot_transaction = len(transaction)
    
    context = {'data' : transaction, 'tot_transaction':tot_transaction, 'book_not':book_not}

    return render(request, 'transaction.html', context)
    