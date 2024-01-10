from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/profile', null=True, blank=True, verbose_name='تصویر آواتار')
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی ایمیل')
    about_user = models.TextField(max_length=500, null=True, blank=True, verbose_name='درباره شخص')
    address = models.TextField(max_length=500, null=True, blank=True, verbose_name='آدرس')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name is not None and self.last_name is not None:
            return self.get_full_name()
        return self.email
