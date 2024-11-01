from django.db import models

# Create your models here.
class AboutMV(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Title',
        blank=False
    )

    description = models.TextField(
        verbose_name='description',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'MV_About'
        verbose_name_plural = 'MV_Abouts'
        ordering = ('id',)

class GalleryMV(models.Model):
    title = models.CharField(
        max_length=35,
        verbose_name='Title',
        blank=False
    )

    photo = models.ImageField(
        max_length=256,
        null=False,
        blank=False,
        verbose_name='photo',
        upload_to='uploads'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'MV_Photo'
        verbose_name_plural = 'MV_Photos'
        ordering = ('id',)

# Este modelo es para ingresar los términos y condiciones de uso de la aplicación
class TermsConditions(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Title',
        blank=False
    )

    description = models.TextField(
        verbose_name='description',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Term_Condition'
        verbose_name_plural = 'Terms_Conditions'
        ordering = ('id',)
