# Generated by Django 3.1.7 on 2021-04-22 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0008_auto_20210418_1921'),
        ('myclasses', '0006_classregister'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classregister',
            name='student_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myaccount.useraccount'),
        ),
    ]
