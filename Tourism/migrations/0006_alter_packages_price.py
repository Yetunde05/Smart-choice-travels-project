# Generated by Django 4.1.4 on 2022-12-07 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tourism', '0005_alter_packages_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='price',
            field=models.DecimalField(decimal_places=8, max_digits=8),
        ),
    ]