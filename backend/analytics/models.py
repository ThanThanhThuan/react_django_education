from django.db import models

class EducationData(models.Model):
    country = models.CharField(max_length=100)
    year = models.IntegerField()
    indicator = models.CharField(max_length=255) # e.g., "Literacy Rate", "Enrollment"
    gender = models.CharField(max_length=20, default='Total') # Male, Female, Total
    value = models.FloatField()

    def __str__(self):
        return f"{self.country} - {self.year} - {self.value}"