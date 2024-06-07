from django.contrib import admin
from .models import Author, Book, Manage, Publisher

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Manage)
admin.site.register(Publisher)
