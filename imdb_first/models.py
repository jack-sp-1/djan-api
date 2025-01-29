from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# class Movie(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=200)
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name
#



class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    #avg_rating = models.FloatField(default=0)
    #number_rating = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
class Review(models.Model):
    #title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    watchList = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    #user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # comments = models.TextField()
    # likes = models.IntegerField(default=0)
    # dislikes = models.IntegerField(default=0)
    # number_rating = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.rating) + " | " + self.watchList.title