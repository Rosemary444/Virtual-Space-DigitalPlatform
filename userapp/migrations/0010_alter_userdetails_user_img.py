# Generated by Django 4.2.7 on 2023-12-23 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0009_alter_userdetails_user_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='user_img',
            field=models.ImageField(blank=True, default='image.png', upload_to='userimages/'),
        ),
    ]
