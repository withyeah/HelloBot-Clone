from django.db import models
# Create your models here.

class Scenario(models.Model):
    input_message = models.CharField(max_length=255)
    output_message = models.TextField()
    next_question = models.CharField(max_length=255, blank=True)

class Tarot(models.Model):
    card_number = models.IntegerField(unique=True)
    card_image = models.ImageField()
    explanation = models.TextField()

    def __str__(self):
        return f'{self.card_number}'
