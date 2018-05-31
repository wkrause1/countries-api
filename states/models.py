from django.db import models
from countries.models import Country


class State(models.Model):
    state_text = models.CharField(max_length=200)
    state_code = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return (self.state_text + " " + self.state_code)

