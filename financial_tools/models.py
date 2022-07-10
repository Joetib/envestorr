from django.db import models

# Create your models here.


class Currency(models.Model):
    name = models.CharField(max_length=200, blank=True)
    symbol = models.CharField(max_length=20)
    rate = models.DecimalField(decimal_places=10, default=0, blank=True, max_digits=25)

    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    

