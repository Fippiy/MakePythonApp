# Generated by Django 2.1.5 on 2019-01-22 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictweet', '0002_auto_20190121_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictweet_tweet',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
    ]
