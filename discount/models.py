from django.db import models
from django.utils.translation import ugettext_lazy as _
import random, string


class Store(models.Model):
    name = models.CharField(max_length=128, verbose_name=_('Name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Store')
        verbose_name_plural = _('Stores')


class DiscountType(models.Model):
    TYPE = (
        ('percentage', 'Percentage'),
        ('fixed_price', 'Fixed Price'),
        ('fixed_amount', 'Fixed Amount'),
        ('fixed_number', 'Fixed Number')
    )
    CURRENCY = (
        ('EUR', 'Euro'),
        ('USD', 'Dollar'),
        ('SEK', 'Krona')
    )
    name = models.CharField(max_length=256, null=False, verbose_name=_('Name'))
    value = models.IntegerField(verbose_name=_('Value'), null=False)
    type = models.CharField(choices=TYPE, max_length=15, default='percentage', verbose_name=_('Type'))
    currency = models.CharField(choices=CURRENCY, default='USD', max_length=3, verbose_name=_('Currency'))

    def __str__(self):
        return f"{str(self.value)} - {self.type}"

    class Meta:
        verbose_name = _('Discount Type')
        verbose_name_plural = _('Discount Types')


class Discount(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('used', 'Used'),
        ('active', 'Active')
    )
    create_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Created Date'))
    end_date = models.DateTimeField(verbose_name=_('End Date'), null=True)
    code = models.CharField(max_length=20, verbose_name=_('Discount Code'), unique=True, blank=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=False)
    status = models.CharField(choices=STATUS, default='active', max_length=7, verbose_name=_('Status'))
    # type = models.ForeignKey(DiscountType, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.code} - {self.store.name}"

    class Meta:
        verbose_name = _('Discount')
        verbose_name_plural = _('Discounts')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            self.code = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(7))
            super().save(*args, **kwargs)
        except IntegrityError:
            self.save(*args, **kwargs)