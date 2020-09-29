from django.db import models

# Create your models here.


class Accounts(models.Model):
    user = models.CharField(max_length=50)
    def __str__(self):
        return self.user


class Goals(models.Model):
    accounts = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    goal = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.goal + '   ' + str(self.complete)
