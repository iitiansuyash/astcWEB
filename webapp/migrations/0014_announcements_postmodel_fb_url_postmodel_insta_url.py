# Generated by Django 4.0 on 2022-01-03 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_alter_postmodel_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='postmodel',
            name='fb_url',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='insta_url',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]