# Generated by Django 2.2.7 on 2019-11-24 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_auto_20191121_1505"),
    ]

    operations = [
        migrations.AddField(
            model_name="computer",
            name="computer_str_repr",
            field=models.CharField(editable=False, max_length=200, null=True),
        ),
    ]