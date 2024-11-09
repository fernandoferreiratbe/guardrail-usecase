from src.application.apply_input_file_guardrail_rules_use_case import GuardrailRulesUseCase
from src.domain.entities import InputFile


def test_given_valid_sas_file_should_apply_guard_rail_then_return_true():
    # Arrange
    file_content = """data test; set old_data; run;"""
    input_file = InputFile(file_content=file_content, file_name="my_script.ext")
    use_case = GuardrailRulesUseCase(input_file=input_file)

    # Act
    is_valid = use_case.is_it_a_valid_file()

    # Assert
    assert is_valid, "The file was not recognized as a valid sas"


def test_given_invalid_sas_file_should_apply_guard_rail_then_return_false():
    # Arrange
    file_content = """Content not valid; This isn't 'programming language' syntax."""
    input_file = InputFile(file_content=file_content, file_name="my_script.ext")
    use_case = GuardrailRulesUseCase(input_file=input_file)

    # Act
    is_valid = use_case.is_it_a_valid_file()

    # Assert
    assert not is_valid, "Expected invalid SAS file to be recognized as invalid"
