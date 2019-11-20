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


def list_computer_configurations() -> dict:
    """
    List expected configuration of each motherboard brand.
    The computer_config format is like this:
    {
        'motherboard brand' : [
            'supported processor brand',
            'ram memory slots',
            'max ram memory accepted',
            'integrated graphics'
        ]
    }
    """
    computer_config = {
        "ASUS": ["Intel", 2, 16, False],
        "Gigabyte": ["AMD", 2, 16, False],
        "ASRock": ["Hybrid", 4, 64, True],
    }
    return computer_config


def prepare_data_to_computer_build_validation(data) -> list:
    """
    Get serialized data and returns computer data prepared to validation.
    """
    processor = data["processor_id"]
    memories = data["memory_id"]
    memories_quantity = len(memories)
    total_ram = 0
    for memory in memories:
        total_ram += memory.RAM_size
    has_graphic_card = bool(str(data["graphic_card_id"]))
    return [str(processor), memories_quantity, total_ram, has_graphic_card]


def validate_computer_components(data) -> None:
    """
    Validate computer build.
    The logic of this function is an interation through expected data
    and recepcted data. The iteration compares selected processor with
    expected processor, the amount of ram memory cards selected and the
    total of ram memory selected with expected values and if is
    expected to select a graphic card or no.
    If the motherboard is ASRock Fatal, which accepts Intel or AMD
    processors, it's made a change to string 'hybrid' to expected
    processor and another change in boolean value, which represents
    the graphic card, to pass the last validation condition.
    """
    allowed_computer_config_dict = list_computer_configurations()
    config_to_validate = prepare_data_to_computer_build_validation(data)
    motherboard_brand = str(data["motherboard_id"])
    
    for mb_brand, config in allowed_computer_config_dict.items():
        if mb_brand in motherboard_brand:
            allowed_hardware = config
    if motherboard_brand == "ASRock Fatal":
        allowed_hardware[0] = config_to_validate[0]
        config_to_validate[-1] = not config_to_validate[-1]
    for index, selected_hardware in enumerate(config_to_validate):
        if isinstance(selected_hardware, str):
            if not allowed_hardware[index] in selected_hardware:
                raise serializers.ValidationError(
                    f"{motherboard_brand} Motherboards are only compatible with "
                    f"{allowed_hardware[index]} Processors. "
                    f"You selected an {selected_hardware} processor."
                )
        elif index == 1:
            if selected_hardware > allowed_hardware[index]:
                raise serializers.ValidationError(
                    f"Computers with {motherboard_brand} motherboard shouldn't have more "
                    f"than {allowed_hardware[index]} ram memory cards. "
                    f"You selected {selected_hardware} memory cards."
                )
        elif index == 2:
            if selected_hardware > allowed_hardware[index]:
                raise serializers.ValidationError(
                    f"{motherboard_brand} motherboard can't accept more than "
                    f"{allowed_hardware[index]}GB ram memory. "
                    f"You selected a total of {selected_hardware}GB ram memory."
                )
        elif isinstance(selected_hardware, bool):
            if selected_hardware == allowed_hardware[index]:
                raise serializers.ValidationError(
                    f"Computers with {motherboard_brand} motherboard must have "
                    "a graphic card associated with it. Pick one."
                )
