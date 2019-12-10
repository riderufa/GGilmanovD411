from django.db import models

# Create your models here.
class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name

class Publishing(models.Model):
    publishing_name = models.TextField()

    def __str__(self):
        return self.publishing_name

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publishing = models.ForeignKey(Publishing, on_delete=models.CASCADE, null=True, blank=True)
    copy_count = models.BigIntegerField(default=1)
    price = models.DecimalField(default=0, max_digits=19, decimal_places=2)

    def __str__(self):
        return self.title

    def author_full_name(obj):
        return obj.author.full_name

