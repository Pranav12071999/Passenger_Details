from django.db import models

# Create your models here.
class PassengerModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    reward_points = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name + self.reward_points