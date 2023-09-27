from django.db import models

# Create your models here.

class MealsData(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=False)
    description = models.TextField(max_length=300)

    class Meta:
        verbose_name_plural = "Meal"

    def __str__(self):
        return self.name