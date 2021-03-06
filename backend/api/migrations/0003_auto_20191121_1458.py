# Generated by Django 2.2.7 on 2019-11-21 17:58

from django.db import migrations


def create_motherboards(apps, schema_editor) -> None:
    """
    Create motherboards to populate database.
    """
    MotherBoard = apps.get_model("api", "MotherBoard")
    [
        MotherBoard(
            motherboard_description="ASUS Prime",
            supported_processors="Intel",
            slots_ram=2,
            max_ram_supported=16,
            integrated_graphic=False,
        ).save(),
        MotherBoard(
            motherboard_description="Gigabyte",
            supported_processors="AMD",
            slots_ram=2,
            max_ram_supported=16,
            integrated_graphic=False,
        ).save(),
        MotherBoard(
            motherboard_description="ASRock Fatal",
            supported_processors="Hybrid",
            slots_ram=4,
            max_ram_supported=64,
            integrated_graphic=True,
        ).save(),
    ]


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_auto_20191121_1356"),
    ]

    operations = [migrations.RunPython(create_motherboards)]
