# Generated by Django 2.2.1 on 2019-07-18 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('querymanager', '0006_auto_20190717_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='programmer',
            name='hire_date',
            field=models.DateField(null=True),
        ),
    ]
