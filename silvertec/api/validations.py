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
    integrated_video = data["integrated_video"]
    specifications = (supported_processor, slots_RAM, max_RAM, integrated_video)
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
        Integrated video: No (or False)
        """
    elif "Gigabyte" in description:
        real_specifications = real_gigabyte_specifications
        possible_error_message = """
        Gigabyte motherboard must have this configuration:
        Supported processors: AMD
        RAM memory slots: 2
        Max RAM supported: 16GB
        Integrated video: No (or False)
        """
    elif "ASRock" in description:
        real_specifications = real_asrock_specifications
        possible_error_message = """
        ASRock Fatal motherboard must have this configuration:
        Supported processors: Hybrid (Intel or AMD)
        RAM memory slots: 4
        Max RAM supported: 64GB
        Integrated video: Yes (or True)
        """
    for index, item in enumerate(specifications):
        if specifications[index] != real_specifications[index]:
            raise serializers.ValidationError(
                "You selected incorrect configuration. Please try again."
                f"Error message: {possible_error_message}"
            )


def validate_computers_components(data) -> None:
    motherboard = data['motherboard_id']
    processor = data['processor_id']
    video_card = data['video_card_id']
    memories = data['memory_id']
    if 'ASUS' in str(motherboard):
        if 'AMD' in str(processor):
            raise serializers.ValidationError(
                "ASUS Motherboards are only compatible with Intel Processors"
            )