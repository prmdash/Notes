from django.db import models


# Create your models here.
class Profile(models.Model):
    first_name: str = models.CharField(
        max_length=20
    )

    last_name: str = models.CharField(
        max_length=20
    )

    age: int = models.IntegerField()


class Note(models.Model):
    title: str = models.CharField(
        max_length=30
    )

    image_url: str = models.URLField()
    content: str = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

