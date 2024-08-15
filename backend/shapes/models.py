from django.db import models

# Create your models here.

SHAPE_CHOICES = (
    ('1', 'Sphere'),
    ('2', 'box'),
    ('3', 'cylinder'),
)

class Shape(models.Model):
    type = models.CharField(max_length=2, choices=SHAPE_CHOICES, default='1')
    color = models.CharField(max_length=7, default='#FF00FF', help_text='hex')  

    def __str__(self):
        return str(self.id)
    

   