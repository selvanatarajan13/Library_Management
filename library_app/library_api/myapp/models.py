from django.db import models
import json

# Create your models here.


# Book model

class Book(models.Model):

    bookID = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(blank=True,max_length=200)
    authors = models.CharField(blank=True,max_length=200)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2)
    isbn = models.CharField(max_length=20)
    isbn13 = models.CharField(max_length=20)
    language_code = models.CharField(max_length=20)
    num_pages = models.IntegerField()
    ratings_count = models.IntegerField()
    text_reviews_count = models.IntegerField()
    publication_date = models.DateField(auto_now_add=True)
    publisher = models.CharField(blank=True,max_length=100)

    # show the author name on database
    def __str__(self):
        return self.authors

# member model

class members(models.Model):

    reference_id = models.CharField(max_length=200)
    member_name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    no_of_rental = models.CharField(max_length=20)

    # show the author name on database

    def __str__(self):
        return self.member_name


class Transaction(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    issue_book = models.CharField(max_length=255)
    issue_book_author = models.CharField(max_length=255)
    issue_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name