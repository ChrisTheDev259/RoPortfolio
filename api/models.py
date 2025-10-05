from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    body = models.TextField()
    items_data = models.JSONField(default=list)

    def __str__(self):
        return self.title

class Portfolio_Item(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='portfolio_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.name