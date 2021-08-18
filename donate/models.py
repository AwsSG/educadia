from django.db import models


class Donate(models.Model):
    """
    donation model containing information about donations
    """
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Donation'
        verbose_name_plural = 'Donations'

    def __str__(self):
        return self.name
