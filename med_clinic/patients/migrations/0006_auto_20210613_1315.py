# Generated by Django 3.2.2 on 2021-06-13 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_doctor_secretary'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='gender',
            field=models.CharField(choices=[('F', 'female'), ('M', 'male')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('F', 'female'), ('M', 'male')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='secretary',
            name='gender',
            field=models.CharField(choices=[('F', 'female'), ('M', 'male')], max_length=10, null=True),
        ),
    ]
