# Generated by Django 3.2.2 on 2021-06-02 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0002_consultation_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='cons_type',
            field=models.CharField(choices=[(1, 'Urjent'), (2, 'Normal')], max_length=50),
        ),
    ]
