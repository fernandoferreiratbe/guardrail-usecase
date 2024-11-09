import re

from src.domain.entities import InputFile


class GuardrailRulesUseCase:

    def __init__(self, input_file: InputFile):
        self.input_file = input_file

    def __has_the_right_extension(self) -> bool:
        return self.input_file.file_name.lower().endswith('ext')

    def __has_valid_content(self) -> bool:
        # Define regular expression to verify any correspondence
        pattern = r'\b(proc|run|set|include|quit|data)\b'

        match = re.search(pattern, self.input_file.file_content, re.IGNORECASE)

        return bool(match)

    def is_it_a_valid_file(self) -> bool:
        return self.__has_the_right_extension() and self.__has_valid_content()
