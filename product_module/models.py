from django.db import models
from django.urls import reverse
from account_module.models import User


class ProductCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url_title = models.CharField(max_length=200, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['is_active']
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['url_title']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_delete']),
        ]
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductBrand(models.Model):
    title = models.CharField(max_length=200, verbose_name='نام برند')
    url_title = models.CharField(max_length=200, verbose_name='نام در url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')

    class Meta:
        ordering = ['is_active']
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['url_title']),
            models.Index(fields=['is_active']),
        ]
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ManyToManyField(ProductCategory, related_name='product_categories', verbose_name='دسته بندی ها')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, related_name='product_brands', blank=True, null=True, verbose_name='برند')
    title = models.CharField(max_length=200, verbose_name='نام محصول')
    slug = models.SlugField(max_length=200, default="", null=False, unique=True, verbose_name='عنوان در url')
    short_description = models.CharField(max_length=500, blank=True, null=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name='توضیحات اصلی')
    price = models.PositiveBigIntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to='images/products', blank=True, null=True, verbose_name='تصویر محصول')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['is_active']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['short_description']),
            models.Index(fields=['description']),
        ]
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def get_absolute_url(self):
        return reverse(viewname='product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class ProductTag(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags', verbose_name='محصول')
    caption = models.CharField(max_length=200, verbose_name='عنوان')

    class Meta:
        ordering = ['caption']
        indexes = [
            models.Index(fields=['caption']),
        ]
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'

    def __str__(self):
        return self.caption


class ProductVisit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='visits', null=True, blank=True, verbose_name='کاربر')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='visits', verbose_name='محصول')
    ip = models.CharField(max_length=30, verbose_name='آی پی کاربر')

    def __str__(self):
        return self.ip

    class Meta:
        ordering = ['ip']
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['product']),
            models.Index(fields=['ip']),
        ]
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدیدهای محصول'


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='galleries', verbose_name='محصول')
    image = models.ImageField(upload_to='images/product-gallery', verbose_name='تصویر')

    def __str__(self):
        return self.product.title

    class Meta:
        ordering = ['product']
        indexes = [
            models.Index(fields=['product']),
        ]
        verbose_name = 'تصویر گالری'
        verbose_name_plural = 'گالری تصاویر'
