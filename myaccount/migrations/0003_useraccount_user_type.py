# Generated by Django 3.1.7 on 2021-04-05 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0002_auto_20210401_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='user_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
