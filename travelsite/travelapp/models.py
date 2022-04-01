from django.db import models

# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    des = models.TextField()

    def __str__(self):
        return self.name
class Newupdates(models.Model):
    content = models.CharField(max_length=500)
    update_img = models.ImageField(upload_to='pics')
    update_date = models.DateTimeField()

