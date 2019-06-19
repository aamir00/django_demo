from django.db import models
from django.utils import timezone

# Create your models here.

class Comments(models.Model):
    """docstring for Comments """
    name=models.CharField(max_length=20)
    comment = models.TextField()
    date_added = models.DateTimeField(default= timezone.now )

    def __str__(self):
        return 'id: {} , name: {}, comment: {}'.format(self.id,self.name,self.comment)
