from rest_framework import serializers


def validate_processor(data) -> None:
    """
    Validate processor specifications when adding to database.
    """
    description = data["processor_description"]
    brand = data["processor_brand"]
    if "Intel" in description and brand == "AMD":
        raise serializers.ValidationError(
            "Intel processors can't be associated with AMD brand. Retry."
        )
    elif "AMD" in description and brand == "Intel":
        raise serializers.ValidationError(
            "AMD processors can't be associated with Intel brand. Retry."
        )


def validate_motherboard(data) -> None:
    """
    Validate motherboard specifications when adding to database.
    """
    description = data["motherboard_description"]
    supported_processor = data["supported_processors"]
    slots_RAM = data["slots_RAM"]
    max_RAM = data["max_RAM_supported"]
    integrated_graphic = data["integrated_graphic"]
    specifications = (supported_processor, slots_RAM, max_RAM, integrated_graphic)
    real_asus_specifications = ("Intel", 2, 16, False)
    real_gigabyte_specifications = ("AMD", 2, 16, False)
    real_asrock_specifications = ("Hybrid", 4, 64, True)
    if "ASUS" in description:
        real_specifications = real_asus_specifications
        possible_error_message = """
        ASUS Prime motherboard must have this configuration:
        Supported processors: Intel
        RAM memory slots: 2
        Max RAM supported: 16GB
        Integrated graphic: No (or False).
        """
    elif "Gigabyte" in description:
        real_specifications = real_gigabyte_specifications
        possible_error_message = """
        Gigabyte motherboard must have this configuration:
        Supported processors: AMD
        RAM memory slots: 2
        Max RAM supported: 16GB
        Integrated graphic: No (or False).
        """
    elif "ASRock" in description:
        real_specifications = real_asrock_specifications
        possible_error_message = """
        ASRock Fatal motherboard must have this configuration:
        Supported processors: Hybrid (Intel or AMD)
        RAM memory slots: 4
        Max RAM supported: 64GB
        Integrated graphic: Yes (or True).
        """
    for index, item in enumerate(specifications):
        if specifications[index] != real_specifications[index]:
            raise serializers.ValidationError(
                "You selected incorrect configuration. Please try again."
                f"Error message: {possible_error_message}"
            )


def validate_processor_compatibility_with_motherboard(data) -> None:
    """
    If processor incompatible with motherboard this validation function
    raises an exception.
    """
    motherboard = data["motherboard_id"].motherboard_description
    expected_processor = data["motherboard_id"].supported_processors
    ordered_processor = data["processor_id"].processor_description

    if expected_processor not in ordered_processor:
        if "ASRock" not in motherboard:
            raise serializers.ValidationError(
                f"You selected incorrect processor for your {motherboard} "
                f"motherboard. {motherboard} is only compatible with "
                f"{expected_processor} processors."
            )


def validate_memory_cards_and_motherboard_ram_slots(data) -> None:
    """
    If the quantity of ram memory cards chosen is greater than
    the motherboard ram slots, this validation function raises an
    exception.
    """
    motherboard = data["motherboard_id"].motherboard_description
    expected_quantity_of_ram_cards = data["motherboard_id"].slots_RAM
    ordered_quantity_of_ram_cards = len(data["memory_id"])
    if ordered_quantity_of_ram_cards > expected_quantity_of_ram_cards:
        raise serializers.ValidationError(
            "You selected incorrect number of ram memory cards for your "
            f"computer. {motherboard} motherboard only have "
            f"{expected_quantity_of_ram_cards} ram slots. "
            f"You selected {ordered_quantity_of_ram_cards}."
        )
