from django.db import models

from django.db import models
from django.utils.safestring import mark_safe


class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Dish(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='dishes'
                                 )
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(blank=True, upload_to='images')

    class Meta:
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""


