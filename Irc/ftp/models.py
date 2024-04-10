from django.db import models

# Create your models here.
class Subject(models.Model) :
      name = models.CharField(max_length=100)
      description = models.TextField()
      image = models.ImageField(upload_to="ftp/images")
      
      def __str__(self):
        return self.name
    
class TrainingProgram(models.Model) :
    title = models.CharField(max_length=100)
    description = models.TextField()
    
        
    def __str__(self):
        return self.title
    
class NetworkExpansion(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='network_images/', null=True, blank=True)

    def __str__(self):
        return self.title
    
class Card(models.Model):
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='card_images/')
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.author

class Review(models.Model):
    author = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='review_images/')

    def __str__(self):
        return self.author
    
class Game(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='game_images/', default='2111.w039.n003.5B.p1.5.jpg')
    description = models.TextField()

    def __str__(self):
        return self.title