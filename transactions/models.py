from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    balance = models.FloatField()
    def __unicode__(self):
        return self.name;
    def topUp(self, amount):
        self.balance+=amount;
    def cashOut(self, amount):
        self.balance-=amount;


class Transaction(models.Model):
    user = models.ForeignKey(User)
    time = models.DateTimeField('Transaction happened')
    amount = models.FloatField();
    endBalance = models.FloatField();
    def __unicode__(self):
        return "Debit $"
