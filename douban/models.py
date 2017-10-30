from django.db import models

# Create your models here.
class MovieStar(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    title = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    type = models.CharField(max_length=25)
    country = models.CharField(max_length=20)
    score = models.DecimalField(max_digits=2,decimal_places=1)
    starring = models.TextField()
    def image(self):
        return '<img src="%s"/>' % self.img
    image.allow_tags = True


    def __str__(self):
        return self.title

class Starring(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    actor = models.CharField(max_length=100)
    count = models.IntegerField(max_length=255)
    movie = models.CharField(max_length=2000)

    def __str__(self):
        return self.actor
