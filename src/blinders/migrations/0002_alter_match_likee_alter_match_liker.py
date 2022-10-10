# Generated by Django 4.1.2 on 2022-10-10 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blinders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='likee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likee_id', to='blinders.profile'),
        ),
        migrations.AlterField(
            model_name='match',
            name='liker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liker_id', to='blinders.profile'),
        ),
    ]
