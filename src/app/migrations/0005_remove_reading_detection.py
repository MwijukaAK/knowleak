# Generated by Django 3.1.2 on 2020-10-29 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201029_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reading',
            name='detection',
        ),
    ]