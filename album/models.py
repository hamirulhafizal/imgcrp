from django.db import models


class Photo(models.Model):
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.ImageField()

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'
