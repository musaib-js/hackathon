# Generated by Django 3.2.4 on 2021-09-12 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='skills',
            field=models.CharField(default='', max_length=150),
        ),
    ]
