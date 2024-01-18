from django.db import models
from jalali_date import date2jalali
from account_module.models import User


class ArticleCategory(models.Model):
    parent = models.ForeignKey('ArticleCategory', on_delete=models.CASCADE, blank=True, null=True, verbose_name='دسته بندی والد')
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    url_title = models.CharField(max_length=200, unique=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی های مقاله'


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='نویسنده')
    selected_categories = models.ManyToManyField(ArticleCategory, verbose_name='دسته بندی ها')
    title = models.CharField(max_length=500, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=500, allow_unicode=True, verbose_name='عنوان در url')
    short_description = models.TextField(max_length=500, verbose_name='توضیحات کوتاه')
    text = models.TextField(max_length=5000, verbose_name='متن مقاله')
    image = models.ImageField(upload_to='images/articles', verbose_name='تصویر مقاله')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')

    class Meta:
        ordering = ['-create_date']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['-create_date']),
        ]
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title

    def get_jalali_create_date(self):
        return date2jalali(self.create_date)

    def get_jalali_create_time(self):
        return self.create_date.strftime('%H:%M')


class ArticleComment(models.Model):
    parent = models.ForeignKey('ArticleComment', on_delete=models.CASCADE, blank=True, null=True, verbose_name='والد')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    text = models.TextField(max_length=1000, verbose_name='متن نظر')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'نظر مقاله'
        verbose_name_plural = 'نظرات مقاله'
