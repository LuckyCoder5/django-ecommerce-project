# Generated by Django 3.1.4 on 2021-02-09 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
    ]
