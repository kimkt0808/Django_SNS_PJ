# Generated by Django 4.2 on 2023-09-18 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profileapp", "0002_alter_profile_introduction"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(default="DI.PNG", null=True, upload_to="profile/"),
        ),
    ]
