# Generated by Django 2.1.5 on 2019-01-21 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictweet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictweet_tweet',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]