# Generated by Django 2.2.4 on 2019-12-30 11:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20191230_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
