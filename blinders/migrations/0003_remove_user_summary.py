# Generated by Django 4.1.2 on 2022-10-05 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blinders', '0002_alter_user_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='summary',
        ),
    ]