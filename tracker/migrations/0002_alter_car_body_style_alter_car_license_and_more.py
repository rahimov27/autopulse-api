# Generated by Django 4.2.13 on 2024-05-26 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='body_style',
            field=models.CharField(choices=[('sedan', 'Sedan'), ('coupe', 'Coupe'), ('sports car', 'Sports car'), ('station wagon', 'Station wagon'), ('hatchback', 'Hatchback'), ('convertible', 'Convertible'), ('suv', 'SUV'), ('minivan', 'Minivan'), ('pickup truck', 'Pickup truck')], default='sedan', max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='license',
            field=models.CharField(choices=[('provided', 'Provided'), ('not provided', 'Not Provided')], default='provided', max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='status',
            field=models.CharField(choices=[('ready', 'Ready'), ('leased', 'Leased'), ('repair', 'In Repair')], default='ready', max_length=20),
        ),
    ]
