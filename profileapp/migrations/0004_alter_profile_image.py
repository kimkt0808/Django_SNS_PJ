# Generated by Django 4.2 on 2023-09-18 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profileapp", "0003_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(null=True, upload_to="profile/"),
        ),
    ]
