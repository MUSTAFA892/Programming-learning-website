from django.db import models

class Me(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length =100)
