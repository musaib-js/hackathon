# Generated by Django 3.2.4 on 2021-09-18 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_notification_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='timestamp',
            field=models.DateField(default='01-01-2020'),
        ),
    ]
