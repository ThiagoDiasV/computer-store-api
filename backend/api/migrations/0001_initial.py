# Generated by Django 2.2.7 on 2019-11-21 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Computer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GraphicCard",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "graphic_card_description",
                    models.CharField(
                        choices=[
                            (
                                "Gigabyte Geforce GTX 1060 6GB",
                                "Gigabyte Geforce GTX 1060 6GB",
                            ),
                            ("PNY RTX 2060 6GB", "PNY RTX 2060 6GB"),
                            ("Radeon RX 580 8GB", "Radeon RX 580 8GB"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Memory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ram_description",
                    models.CharField(
                        choices=[("Hiper X", "Hiper X")], max_length=10
                    ),
                ),
                (
                    "ram_size",
                    models.PositiveIntegerField(
                        choices=[
                            (4, "4"),
                            (8, "8"),
                            (16, "16"),
                            (32, "32"),
                            (64, "64"),
                        ]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MotherBoard",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "motherboard_description",
                    models.CharField(
                        choices=[
                            ("ASUS Prime", "Asus Prime"),
                            ("Gigabyte", "Gigabyte"),
                            ("ASRock Fatal", "ASRock Fatal"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "supported_processors",
                    models.CharField(
                        choices=[
                            ("Intel", "Intel"),
                            ("AMD", "AMD"),
                            ("Hybrid", "Hybrid"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "slots_ram",
                    models.PositiveIntegerField(choices=[(2, "2"), (4, "4")]),
                ),
                (
                    "max_ram_supported",
                    models.PositiveIntegerField(
                        choices=[(16, "16 GB"), (64, "64 GB")]
                    ),
                ),
                ("integrated_graphic", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Processor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "processor_description",
                    models.CharField(
                        choices=[
                            ("Intel Core i5", "Intel Core i5"),
                            ("Intel Core i7", "Intel Core i7"),
                            ("AMD Athlon", "AMD Athlon"),
                            ("AMD Ryzen 7", "AMD Ryzen 7"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "processor_brand",
                    models.CharField(
                        choices=[("Intel", "Intel"), ("AMD", "AMD")],
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("computer_id", models.ManyToManyField(to="api.Computer")),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="computer",
            name="graphic_card_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.GraphicCard",
            ),
        ),
        migrations.AddField(
            model_name="computer",
            name="memory_id",
            field=models.ManyToManyField(to="api.Memory"),
        ),
        migrations.AddField(
            model_name="computer",
            name="motherboard_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="api.MotherBoard",
            ),
        ),
        migrations.AddField(
            model_name="computer",
            name="processor_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.Processor"
            ),
        ),
    ]
