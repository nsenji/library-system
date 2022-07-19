from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
from datetime import *
from django.contrib.auth.models import User

# Create your models here.
"""Model that stores the library books"""
class Book(models.Model):
  CATEGORY = [
    ('education', 'Education'),
    ('comics', 'Comics'),
    ('biography', 'Biography'),
    ('history', 'History'),
    ('novel', 'Novel'),
    ('fantasy', 'Fantasy'),
    ('thriller', 'Thriller'),
    ('romance', 'Romance'),
    ('scifi','Sci-Fi')
  ]
  
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  category = models.CharField(max_length=40, choices = CATEGORY)
  status = models.BooleanField(default = True)
  description = models.TextField(max_length=3000)
  image = models.ImageField(upload_to = 'pics', blank = True)
  class Meta:
    verbose_name_plural = 'books'


  def __str__(self):
    return self.title

"""Model for the Users borrowing books"""
class Borrower(models.Model):
  first_name = models.CharField(max_length=300)
  last_name = models.CharField(max_length=300)
  username = models.CharField(max_length=300)
  book_name = models.CharField(max_length=300)
  reg_no = models.CharField(max_length=200)
  class Meta:
    verbose_name_plural = 'borrowers'

  def __str__(self):
    return str(self.username)+"["+str(self.book_name)+']'

"""Function to define the return date of the book"""
def get_return_date():
  return datetime.now() + timedelta(hours = 1)

"""Function to define the amount of time for the user to pick the book"""
def book_time_limit():
  return datetime.now() + timedelta(hours=6) 

"""Model for the books issued to a borrower"""
class IssuedBook(models.Model):
  book_name = models.ForeignKey(Book, null = True , on_delete=models.CASCADE)
  borrower = models.ForeignKey(Borrower, null = True , on_delete=models.CASCADE)
  reg_no = models.CharField(max_length=200)
  issued_date = models.DateField(auto_now = True)
  return_date = models.DateField(auto_now = True) 
  class Meta:
    verbose_name_plural = 'issuedbooks'

  def __str__(self):
    return str(self.book_name)+ ' ' +'[' + str(self.borrower) + ']' 


"""Model for the  book requested by the borrower"""
class RequestedBook(models.Model):
  # book_request = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='requested_book_num')
  book_name = models.CharField(max_length= 200)
  return_date = models.DateField(default=get_return_date)
  pickup_time = models.DateTimeField(default=book_time_limit)
  borrower = models.CharField(max_length= 200)
  class Meta:
    verbose_name_plural = 'requestedbooks'

  def __str__(self):
    return str(self.book_name) + '(' + str(self.borrower) + ')'

  # def number_of_requested_books(self):
  #   if self.book_request.count() < 3:
  #     return self.book_request.count()
  #   else:
  #     return "Unable to borrow more than two books."

  


class Returned_book(models.Model):
  borrower = models.ForeignKey(Borrower,on_delete= models.CASCADE)
  book_name = models.ForeignKey(IssuedBook,on_delete= models.CASCADE)
  date_of_return = models.DateTimeField(auto_now = True)
  reg_no = models.BigIntegerField()
  user = models.ForeignKey(User,on_delete= models.CASCADE)
  return_date = models.DateField(auto_now = True)

  # def __str__(self):
  #   return self.book_name + '[' + self.borrower + ']'
  def __str__(self):
    return self.user


  

  
