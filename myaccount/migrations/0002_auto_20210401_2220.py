# Generated by Django 3.1.7 on 2021-04-01 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='email',
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='first_names',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
