# Generated by Django 5.1.7 on 2025-03-19 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "sid",
                    models.PositiveBigIntegerField(primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=100)),
                ("emailid", models.EmailField(max_length=20)),
            ],
        ),
    ]
