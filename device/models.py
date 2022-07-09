from django.db import models

# Create your models here.

class devices(models.Model):
    id = models.AutoField(primary_key=True)
    route = models.CharField(max_length=70)

    def __str__(self):
        return self.route
