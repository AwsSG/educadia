from django.db import models
from myaccount.models import UserAccount


class AllClasses(models.Model):
    """
    The main classes model, contains all the availale classes
    """
    added_by = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=100, null=False, blank=False)
    class_subject = models.CharField(max_length=100, null=False, blank=False)
    class_university = models.CharField(max_length=100, null=False, blank=False)
    class_collage = models.CharField(max_length=100, null=False, blank=False)
    class_department = models.CharField(max_length=100, null=False, blank=False)
    class_level = models.CharField(max_length=100, null=False, blank=False)
    class_division = models.CharField(max_length=100, null=False, blank=False)
    class_year = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.class_name or ''
