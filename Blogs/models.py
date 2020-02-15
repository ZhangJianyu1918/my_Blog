from django.db import models

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.text

class Blog(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    text = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        verbose_name_plural='Blog'

    def __str__(self):
        return self.text[:20] + '...'
    

    

    
    


    


