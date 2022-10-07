# Generated by Django 4.1.2 on 2022-10-07 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blinders', '0004_rename_display_name_profile_first_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='matchee_id',
            new_name='likee_id',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='matcher_id',
            new_name='liker_id',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='first_name',
            new_name='display_name',
        ),
        migrations.AddField(
            model_name='match',
            name='date_confirmed',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='blurred_profile_picture_url',
            field=models.ImageField(blank=True, default='media/images/default_profile_picture.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture_url',
            field=models.ImageField(blank=True, default='media/images/default_profile_picture.jpg', upload_to='images/'),
        ),
    ]
