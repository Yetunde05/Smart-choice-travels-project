# Generated by Django 4.1.4 on 2022-12-09 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tourism', '0016_alter_destination_countries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='country',
            field=models.CharField(max_length=100),
        ),
    ]
