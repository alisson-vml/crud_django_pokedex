from django.db import models

class Pokemon(models.Model):
  nome= models.CharField(max_length=100)
  foto_url = models.URLField(null=True, blank=True)
  
  def __str__(self):
    return self.nome