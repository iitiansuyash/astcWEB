# Generated by Django 4.0 on 2021-12-29 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='body',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
