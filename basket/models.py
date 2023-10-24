from django.db import models

class Basket(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image_url = models.URLField(default='https://www.aldi-nord.de/sortiment/backwaren-aufstriche-cerealien/brotaufstrich/bio-konfituere-extra-2977-0-0.article.html')
    
    def __str__(self):
        return self.name + ' ' + self.description