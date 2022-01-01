# Generated by Django 4.0 on 2021-12-31 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_teammember_fb_url_teammember_insta_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='profile_pic',
            field=models.ImageField(upload_to='./members'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='status',
            field=models.CharField(choices=[('Coordinator', 'Coordinator'), ('Member', 'Member'), ('Founder', 'Founder'), ('Alumnus', 'Alumnus')], default=0, max_length=100),
            preserve_default=False,
        ),
    ]
