# Generated by Django 4.2.3 on 2023-11-24 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_rename_discreption_products_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='code',
            field=models.CharField(max_length=7, null=True),
        ),
    ]
