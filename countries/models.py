from django.db import models

class Country(models.Model):
    country_text = models.CharField(max_length=200)
    country_code = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.country_text


