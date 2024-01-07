from django.db import models
from django.utils import timezone
from django.utils.html import format_html


class ContactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    full_name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    message = models.TextField(max_length=1000, verbose_name='متن تماس با ما')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    response = models.TextField(blank=True, null=True, verbose_name='متن پاسخ تماس با ما')
    is_read_by_admin = models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین')

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    image = models.ImageField(upload_to='images', verbose_name='تصویر')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')

    class Meta:
        ordering = ['-created']
        verbose_name = 'عکس پروفایل کاربر'
        verbose_name_plural = 'لیست عکس پروفایل کاربر'

    def __str__(self):
        return self.image.name

    def get_image_file(self):
        return format_html(f"<img src='{self.image.url}' alt='{self.image.name}' width='50' href='70'>")
