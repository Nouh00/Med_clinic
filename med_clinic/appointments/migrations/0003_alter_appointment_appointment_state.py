# Generated by Django 3.2 on 2021-05-07 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_auto_20210505_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_state',
            field=models.CharField(choices=[(True, 'Approved'), (False, 'Pending')], max_length=10),
        ),
    ]
