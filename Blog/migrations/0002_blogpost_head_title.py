# Generated by Django 3.0.4 on 2020-04-28 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='Head_title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
