# Generated by Django 5.1.7 on 2025-04-01 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='petname',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
    ]
