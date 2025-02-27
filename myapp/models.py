from django.db import models



class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    extra_info = models.JSONField(default=dict, blank=True)  # Store extra fields as JSON

    def __str__(self):
        return self.name
