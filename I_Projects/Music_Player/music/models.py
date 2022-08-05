from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.TextField()
    author = models.TextField()
    image = models.ImageField()
    audio_file = models.FileField(blank=True, null=True)    
    audio_link = models.CharField(max_length=200, blank=True, null=True)
    duration = models.CharField(max_length=20)
    paginate_by = 2

    def __str__(self):
        return self.title
#The combo of the two is so frequent because typically if you’re 
#going to allow a field to be blank in your form, you’re going to also need your database to allow NULL values for that field.