from django.db import models

# Create your models here.

class JPY(models.Model):
    date = models.DateTimeField()
    rate_cash_buy = models.FloatField()
    rate_cash_sell = models.FloatField()
    rate_sight_buy = models.FloatField()
    rate_sight_sell = models.FloatField()

class CNY(models.Model):
    date = models.DateTimeField()
    rate_cash_buy = models.FloatField()
    rate_cash_sell = models.FloatField()
    rate_sight_buy = models.FloatField()
    rate_sight_sell = models.FloatField()

class USD(models.Model):
    date = models.DateTimeField()
    rate_cash_buy = models.FloatField()
    rate_cash_sell = models.FloatField()
    rate_sight_buy = models.FloatField()
    rate_sight_sell = models.FloatField()

class EUR(models.Model):
    date = models.DateTimeField()
    rate_cash_buy = models.FloatField()
    rate_cash_sell = models.FloatField()
    rate_sight_buy = models.FloatField()
    rate_sight_sell = models.FloatField()

class GBP(models.Model):
    date = models.DateTimeField()
    rate_cash_buy = models.FloatField()
    rate_cash_sell = models.FloatField()
    rate_sight_buy = models.FloatField()
    rate_sight_sell = models.FloatField()

class AUD(models.Model):
    date = models.DateTimeField()
    rate_cash_buy = models.FloatField()
    rate_cash_sell = models.FloatField()
    rate_sight_buy = models.FloatField()
    rate_sight_sell = models.FloatField()

class SGD(models.Model):
    date = models.DateTimeField()
    rate_cash_buy = models.FloatField()
    rate_cash_sell = models.FloatField()
    rate_sight_buy = models.FloatField()
    rate_sight_sell = models.FloatField()

class KRW(models.Model):
    date = models.DateTimeField()
    rate_cash_buy = models.FloatField()
    rate_cash_sell = models.FloatField()
    rate_sight_buy = models.FloatField()
    rate_sight_sell = models.FloatField()