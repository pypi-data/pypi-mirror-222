# Generated by Django 3.2.4 on 2021-06-15 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 17, 0, 0), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='how are you?', max_length=200),
        ),
    ]
