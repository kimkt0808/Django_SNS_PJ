# Generated by Django 4.2 on 2023-09-18 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profileapp", "0006_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                default="/media/DI.PNG", null=True, upload_to="profile/"
            ),
        ),
    ]
