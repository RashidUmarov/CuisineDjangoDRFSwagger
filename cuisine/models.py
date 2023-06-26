from django.db import models


class Category(models.Model):
    """Категория блюда"""
    title = models.CharField('Название категории', max_length=50)
    description = models.TextField('Описание', max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Dish(models.Model):
    """Название блюда"""
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='dishes',
                                 verbose_name="Категория",
                                 )
    title = models.TextField('Название', max_length=100)
    description = models.TextField('Описание', max_length=500)
    image = models.ImageField('Фото', blank=True, upload_to='images')

    class Meta:
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.title
