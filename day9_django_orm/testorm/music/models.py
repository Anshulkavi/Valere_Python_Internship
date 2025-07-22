from django.db import models

# Create your models here.
from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Song(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Django ORM Query Methods Summary
# .all(): Retrieve all objects of a model.
# .filter(): Retrieve objects that match the given conditions.
# .exclude(): Retrieve objects that do not match the given conditions.
# .get(): Retrieve a single object that matches the given condition (raises an error if more than one object matches).
# .update(): Update multiple objects at once.
# .delete(): Delete records from the database.