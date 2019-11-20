from rest_framework import serializers


def validate_processor(data) -> None:
    """
    Validate processor specifications.
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
    Validate motherboard specifications.
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


def get_serializer_data(data) -> tuple:
    """
    Get the serializer data.
    """
    processor = data["processor_id"]
    graphic_card = data["graphic_card_id"]
    memories = data["memory_id"]
    total_ram = 0
    for memory in memories:
        total_ram += memory.RAM_size
    return (processor, graphic_card, memories, total_ram)


def validate_asus_computer_components(data) -> None:
    extracted_data = get_serializer_data(data)
    processor = extracted_data[0]
    graphic_card = extracted_data[1]
    memories = extracted_data[2]
    total_ram = extracted_data[3]

    if "AMD" in str(processor):
        raise serializers.ValidationError(
            "ASUS Prime Motherboards are only compatible with Intel Processors."
        )
    if len(memories) > 2:
        raise serializers.ValidationError(
            "Computers with ASUS Prime Motherboards shouldn't have more than 2 ram memory cards."
        )
    if total_ram > 16:
        raise serializers.ValidationError(
            "ASUS Prime Motherboards shouldn't accept more than 16GB ram memory."
        )
    if not graphic_card:
        raise serializers.ValidationError(
            "Computers with ASUS Prime MotherBoards must have a graphic card associated with it."
        )


def validate_gigabyte_computer_components(data) -> None:
    extracted_data = get_serializer_data(data)
    processor = extracted_data[0]
    graphic_card = extracted_data[1]
    memories = extracted_data[2]
    total_ram = extracted_data[3]

    if "Intel" in str(processor):
        raise serializers.ValidationError(
            "Gigabyte Motherboards are only compatible with AMD Processors."
        )
    if len(memories) > 2:
        raise serializers.ValidationError(
            "Computers with Gigabyte Motherboards shouldn't have more than 2 ram memory cards."
        )
    if total_ram > 16:
        raise serializers.ValidationError(
            "Gigabyte Motherboards shouldn't accept more than 16GB ram memory."
        )
    if not graphic_card:
        raise serializers.ValidationError(
            "ASUS Prime MotherBoards must have a graphic card associated with it."
        )


def validate_asrock_computer_components(data) -> None:
    extracted_data = get_serializer_data(data)
    processor = extracted_data[0]
    graphic_card = extracted_data[1]
    memories = extracted_data[2]
    total_ram = extracted_data[3]

    if "Intel" in str(processor):
        raise serializers.ValidationError(
            "Gigabyte Motherboards are only compatible with AMD Processors."
        )
    if len(memories) > 2:
        raise serializers.ValidationError(
            "ASUS Prime Motherboards shouldn't have more than 2 memory ram cards."
        )
    if not graphic_card:
        raise serializers.ValidationError(
            "ASUS Prime MotherBoards must have a graphic card associated with it."
        )