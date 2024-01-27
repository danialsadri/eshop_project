from django.db import models
from account_module.models import User
from product_module.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='کاربر')
    payment_date = models.DateField(blank=True, null=True, verbose_name='تاریخ پرداخت')
    is_paid = models.BooleanField(verbose_name='نهایی شده/نشده')

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید کاربران'

    def __str__(self):
        return str(self.user)

    def calculate_total_price(self):
        total_amount = 0
        if self.is_paid:
            for order_detail in self.order_details.all():
                total_amount += order_detail.final_price * order_detail.count
        else:
            for order_detail in self.order_details.all():
                total_amount += order_detail.product.price * order_detail.count
        return total_amount


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_details', verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_details', verbose_name='محصول')
    final_price = models.IntegerField(blank=True, null=True, verbose_name='قیمت نهایی تکی محصول')
    count = models.IntegerField(verbose_name='تعداد')

    class Meta:
        verbose_name = 'جزییات سبد خرید'
        verbose_name_plural = 'لیست جزییات سبدهای خرید'

    def __str__(self):
        return str(self.order)

    def get_total_price(self):
        return self.count * self.product.price
