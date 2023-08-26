from django.db import models


class drug(models.Model):
    brand =  models.CharField(max_length=100)
    name =   models.CharField(max_length=100)
    category = models.CharField(max_length=50,null=True)
    added_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
            return str(self.name)