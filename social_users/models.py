from django.db import models
from django.conf import settings


class Posts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Post_Image = models.ImageField(upload_to='post_images')
    Caption = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.first_name



