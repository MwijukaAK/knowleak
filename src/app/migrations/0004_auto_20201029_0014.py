# Generated by Django 3.1.2 on 2020-10-28 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201028_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='flowrate',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reading',
            name='pressure',
            field=models.IntegerField(default=0),
        ),
    ]