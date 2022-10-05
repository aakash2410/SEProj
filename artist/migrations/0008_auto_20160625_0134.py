# Generated by Django 1.9.7 on 2016-06-25 01:34
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("artist", "0007_artistadmin")]

    operations = [
        migrations.AlterField(
            model_name="artistadmin",
            name="role",
            field=models.CharField(
                choices=[
                    ("musician", "Musician"),
                    ("manager", "Manager"),
                    ("producer", "Producer"),
                    ("songwriter", "Songwriter"),
                ],
                help_text="The relationship of this user to the artist",
                max_length=12,
            ),
        )
    ]
