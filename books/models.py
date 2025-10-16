from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    books_published = models.IntegerField(default=0)
    list_of_books = models.TextField(blank=True)  

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    price = models.DecimalField(max_digits=6, decimal_places=2 ,default=0.00)
    published_date = models.DateField(default=None, null=True, blank=True)
    added_to_site_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
