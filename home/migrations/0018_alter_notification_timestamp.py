# Generated by Django 3.2.4 on 2021-09-19 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_notification_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='timestamp',
            field=models.CharField(default='01-01-2020', max_length=20),
        ),
    ]
