from django.db import models

# Create your models here.

class Scenario(models.Model):
    input_message = models.CharField(max_length=255)
    output_message = models.TextField()
    next_question = models.CharField(max_length=255)

class Tarot(models.Model):
    card_number = models.IntegerField()
    card_image = models.ImageField()
    explanation = models.TextField()

    def __str__(self):
        return self.card_number