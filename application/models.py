from django.db import models

from account.models import Profile


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    name = models.CharField(verbose_name='Наименование товара', max_length=512)
    code = models.IntegerField(verbose_name='Код товара')
    price = models.DecimalField(verbose_name='Цена товара', max_digits=32, decimal_places=2)

    def __repr__(self):
        return '{} {} {}'.format(self.name, self.code, self.price)

class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    user_profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='order_profile', verbose_name='Анкета заказчика')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True, related_name='order_product', verbose_name='Заказанный продукт')
    quantity = models.IntegerField(verbose_name='Количество продукта')
    total_price = models.DecimalField(verbose_name='Итоговая сумма', decimal_places=2, max_digits=32)

    def __repr__(self):
        return '{} {}'.format(self.product, self.quantity)