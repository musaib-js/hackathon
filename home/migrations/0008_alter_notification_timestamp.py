# Generated by Django 3.2.4 on 2021-09-13 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_notification_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='timestamp',
            field=models.DateField(default=1971),
        ),
    ]
