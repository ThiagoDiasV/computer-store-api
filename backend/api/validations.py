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
    slots_ram = data["slots_ram"]
    max_ram = data["max_ram_supported"]
    integrated_graphic = data["integrated_graphic"]
    specifications = (
        supported_processor,
        slots_ram,
        max_ram,
        integrated_graphic,
    )
    real_asus_specifications = ("Intel", 2, 16, False)
    real_gigabyte_specifications = ("AMD", 2, 16, False)
    real_asrock_specifications = ("Hybrid", 4, 64, True)
    if "ASUS" in description:
        real_specifications = real_asus_specifications
        possible_error_message = (
            "ASUS Prime motherboard must have this "
            "configuration: Supported processors: Intel // RAM memory slots: 2"
            " // Max RAM supported: 16GB // Integrated graphic: No (or False)."
        )
    elif "Gigabyte" in description:
        real_specifications = real_gigabyte_specifications
        possible_error_message = (
            "Gigabyte motherboard must have this "
            "configuration: Supported processors: AMD // RAM memory slots: 2 "
            "// Max RAM supported: 16GB // Integrated graphic: No (or False)."
        )
    elif "ASRock" in description:
        real_specifications = real_asrock_specifications
        possible_error_message = (
            "ASRock Fatal motherboard must have this "
            "configuration: Supported processors: Hybrid (Intel or AMD)// "
            "RAM memory slots: 4 // Max RAM supported: 64GB // "
            "Integrated graphic: Yes (or True)."
        )
    for index, item in enumerate(specifications):
        if specifications[index] != real_specifications[index]:
            raise serializers.ValidationError(
                "You selected incorrect configuration. Please try again."
                f" Error message: {possible_error_message}"
            )


def validate_processor_compatibility_with_motherboard(data) -> None:
    """
    If processor is incompatible with motherboard this validation function
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
    expected_quantity_of_ram_cards = data["motherboard_id"].slots_ram
    ordered_quantity_of_ram_cards = len(data["memory_id"])
    if ordered_quantity_of_ram_cards > expected_quantity_of_ram_cards:
        raise serializers.ValidationError(
            "You selected incorrect number of ram memory cards for your "
            f"computer. {motherboard} motherboard only have "
            f"{expected_quantity_of_ram_cards} ram slots. "
            f"You selected {ordered_quantity_of_ram_cards}."
        )


def validate_total_ram_ordered_and_motherboard_ram_support(data) -> None:
    """
    If the total of ordered ram is greater than the motherboard ram support
    this validation function raises an exception.
    """
    motherboard = data["motherboard_id"].motherboard_description
    expected_total_ram = data["motherboard_id"].max_ram_supported
    ordered_total_of_ram = 0
    for memory in data["memory_id"]:
        ordered_total_of_ram += memory.ram_size
    if ordered_total_of_ram > expected_total_ram:
        raise serializers.ValidationError(
            "You choose a total of RAM memory greater than the maximum "
            f"RAM supported by {motherboard} motherboard. "
            f"{motherboard} motherboard only supports {expected_total_ram}GB "
            f"and you chosen {ordered_total_of_ram}GB."
        )


def validate_graphic_card_or_not_in_motherboard(data) -> None:
    """
    If the chosen motherboard does not have integrated video the
    client must choose a graphic card. On the other hand, if the 
    motherboard has integrated video, the client isn't obligated to
    choose a graphic card. This function validates this behavior.
    """
    motherboard = data["motherboard_id"].motherboard_description
    mb_has_integrated_graphics = data["motherboard_id"].integrated_graphic
    if not mb_has_integrated_graphics:
        if not data["graphic_card_id"]:
            raise serializers.ValidationError(
                f"{motherboard} motherboard doesn't have integrated graphics. "
                "You must order a graphic card to your computer."
            )
