# Generated by Django 5.0.6 on 2024-05-22 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0002_alter_movie_duration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="description",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
