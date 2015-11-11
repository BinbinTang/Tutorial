from django.db import models

# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=200)
    balance = models.FloatField()

    def __unicode__(self):
        return self.name

    def topUp(self, amount):
        self.balance += amount

    def deductFrom(self, amount):
        self.balance -= amount


class Transaction(models.Model):
    account = models.ForeignKey(Account)
    time = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    endBalance = models.FloatField()
