from django.db import models

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    check_in_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
