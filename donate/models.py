from django.db import models


class Donate(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=25)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
