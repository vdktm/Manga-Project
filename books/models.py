from django.db import models
from django.core.validators import FileExtensionValidator
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


class Comix(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    description = models.TextField(max_length=500)
    thumbnail = models.ImageField(
        blank=True,
        upload_to='images/thumbnails/',
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))]
    )
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    category = TreeForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'slug': self.slug})


class Category(MPTTModel):

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    description = models.TextField(max_length=300)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_index=True,
        related_name='children',
    )

    class MPTTMeta:
        order_insertion_by = ('title',)

    def get_absolute_url(self):
        """
        Получаем прямую ссылку на категорию
        """
        return reverse('book_by_category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
