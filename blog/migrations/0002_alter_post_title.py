# Generated by Django 4.2.7 on 2023-12-25 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=500, null=True),
        ),
    ]
