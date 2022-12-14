# Generated by Django 4.1.4 on 2022-12-09 15:56

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Tourism', '0012_about_alter_caurosel1_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countries', django_countries.fields.CountryField(max_length=2)),
                ('images', models.ImageField(upload_to='imgs')),
            ],
        ),
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='Caurosel1',
        ),
    ]
