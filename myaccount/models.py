from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserAccount(models.Model):
    """
    The main user model containing information for all user types
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_names = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    user_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserAccount.objects.create(user=instance)
    # Existing users: just save the profile
    instance.useraccount.save()
