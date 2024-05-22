from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='livros')
    title = models.CharField(max_length=40)
    description = models.TextField()
    



