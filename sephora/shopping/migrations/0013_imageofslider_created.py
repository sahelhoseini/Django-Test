# Generated by Django 4.2.3 on 2023-11-27 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0012_imageofslider'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageofslider',
            name='created',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
    ]