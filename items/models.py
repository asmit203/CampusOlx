from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    durationUsed = models.IntegerField(default=0)
    warranty = models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='item_images')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('item-detail',kwargs={'pk':self.pk})