# Generated by Django 3.0.2 on 2020-01-13 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pothole_detection_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accelometer_post',
            name='app_user_field',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pothole_detection_app.app_User'),
        ),
        migrations.AddField(
            model_name='post',
            name='app_user_field',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pothole_detection_app.app_User'),
        ),
    ]
