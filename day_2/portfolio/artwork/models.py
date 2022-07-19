from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __str__(self):
        return self.name


class Artwork(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    creation_date = models.DateField()
    estimated_value = models.FloatField()
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.name


class Multimedia(models.Model):
    type = models.CharField(max_length=100)
    creation_date = models.DateField()

    arwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)

    def __str__(self):
        return self.type

class Portfolio(models.Model):
    name = models.CharField(max_length=100)

    arworklist = models.ManyToManyField(Artwork)

    def __str__(self):
        return self.name


class Exposition(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    description = models.CharField(max_length=200)

    portfolios = models.ManyToManyField(Portfolio)

    def __str__(self):
        return self.name
