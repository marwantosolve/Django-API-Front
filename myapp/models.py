from django.db import models

# Create your models here.

class Book(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  cover = models.ImageField(upload_to='covers/', null=True, blank=True)

  def __str__(self) -> str:
    return self.name