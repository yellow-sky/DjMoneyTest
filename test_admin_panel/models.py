from __future__ import unicode_literals
from django.db import models
from djmoney.models.fields import MoneyField


class SimpleMoneyModel(models.Model):
    pay = MoneyField(decimal_places=2, max_digits=10)


class SimpleMoneyModelProxy(SimpleMoneyModel):
    class Meta:
        proxy = True
