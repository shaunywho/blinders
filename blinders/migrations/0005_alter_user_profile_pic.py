# Generated by Django 4.1.2 on 2022-10-05 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blinders', '0004_alter_user_blurred_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
