# Generated by Django 2.2.12 on 2020-05-10 02:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Banco', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticias',
            name='titulo',
            field=models.CharField(default=datetime.datetime(2020, 5, 10, 2, 1, 42, 664633, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
