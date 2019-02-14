from django.db import models

class Number (models.Model):
    number_text = models.CharField(max_length=10)
    counter_number = models.IntegerField(default=0)
    def __str__(self):
        return self.number_text



