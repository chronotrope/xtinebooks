from django.db import models
from django.contrib import admin

# Create your models here.
class BookPost(models.Model):
    book_title = models.CharField(max_length=150)
    book_author = models.CharField(max_length=150)
    book_desc = models.TextField()
    isbn = models.CharField(max_length=150, blank=True)
    rating = models.IntegerField()
    image_url = models.CharField(max_length=150)
    timestamp = models.DateTimeField()
admin.site.register(BookPost)
    
class BookPostAdmin(admin.ModelAdmin):
    list_dispay = ('book_title', 'timestamp')
