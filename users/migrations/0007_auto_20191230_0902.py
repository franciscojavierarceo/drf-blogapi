# Generated by Django 2.2.4 on 2019-12-30 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20191219_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='verification_code',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]