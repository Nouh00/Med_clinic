# Generated by Django 3.2.2 on 2021-06-05 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0002_auto_20210510_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='secretary',
        ),
    ]
