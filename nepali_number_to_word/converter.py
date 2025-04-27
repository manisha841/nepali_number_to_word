"""
Core number to Nepali word conversion logic
"""

from typing import List
from .constants import (
    UNITS,
    TENS,
    HUNDREDS,
    SPECIAL_NUMBERS,
    NEPALI_NUMERALS,
)

KHARAB = 100000000000
ARAB = 1000000000
CRORE = 10000000
LAKH = 100000
THOUSAND = 1000


class NepaliNumberConverter:
    """Converter for numbers to Nepali words and numerals"""

    def __init__(self):
        self.unit_values = [
            (KHARAB, "खर्ब"),
            (ARAB, "अरब"),
            (CRORE, "करोड"),
            (LAKH, "लाख"),
            (THOUSAND, "हजार"),
        ]

    def convert_to_nepali_words(self, number: int) -> str:
        """
        Convert a number to Nepali words
        Args:
            number: The number to convert
        Returns:
            Nepali words representation of the number
        """
        if number == 0:
            return "शून्य"

        if number < 0:
            return "ऋणात्मक " + self.convert_to_nepali_words(abs(number))

        words: List[str] = []

        for unit_value, unit_name in self.unit_values:
            unit_count = number // unit_value
            if unit_count > 0:
                words.append(self._convert_number_part(unit_count) + " " + unit_name)
                number = number % unit_value

        if number > 0:
            words.append(self._convert_number_part(number))

        result = " ".join(filter(None, words))
        return result.strip() + " रूपैयाँ मात्र"

    def convert_to_nepali_numerals(self, number: int) -> str:
        """
        Convert a number to Nepali numerals with /- suffix and Nepali-style comma formatting
        Args:
            number: The number to convert
        Returns:
            Formatted Nepali numerals with commas and /- suffix
        """
        if number < 0:
            return "-" + self.convert_to_nepali_numerals(abs(number))

        nepali_num = "".join(NEPALI_NUMERALS[digit] for digit in str(number))
        formatted_num = self._format_with_commas(nepali_num)
        return f"{formatted_num} /-"

    def _format_with_commas(self, number_str: str) -> str:
        """
        Format a number string with Nepali-style commas
        Args:
            number_str: The number string to format
        Returns:
            Formatted string with commas
        """
        parts: List[str] = []

        if len(number_str) > 3:
            parts.append(number_str[-3:])
            number_str = number_str[:-3]
        else:
            parts.append(number_str)
            number_str = ""

        while number_str:
            if len(number_str) >= 2:
                parts.append(number_str[-2:])
                number_str = number_str[:-2]
            else:
                parts.append(number_str)
                number_str = ""

        return ",".join(reversed(parts))

    def _convert_number_part(self, number: int) -> str:
        """
        Convert any number part to Nepali words
        Args:
            number: The number to convert
        Returns:
            Nepali words representation of the number
        """
        if number == 0:
            return ""

        if number < 100:
            return self._convert_two_digits(number)
        return self._convert_three_digits(number)

    def _convert_two_digits(self, number: int) -> str:
        """
        Convert a two-digit number to Nepali words
        Args:
            number: The number to convert (0-99)
        Returns:
            Nepali words representation of the number
        """
        if number == 0:
            return ""

        if number < 10:
            return UNITS[number]

        if 10 <= number < 100:
            index = number - 10
            if index < len(SPECIAL_NUMBERS):
                return SPECIAL_NUMBERS[index]

            ten = number // 10
            unit = number % 10
            if unit == 0:
                return TENS[ten]
            return f"{TENS[ten]} {UNITS[unit]}"

        return ""

    def _convert_three_digits(self, number: int) -> str:
        """
        Convert a three-digit number to Nepali words
        Args:
            number: The number to convert (100-999)
        Returns:
            Nepali words representation of the number
        """
        if number == 0:
            return ""

        words: List[str] = []
        hundred = number // 100
        if hundred > 0:
            words.append(HUNDREDS[hundred])

        remaining = number % 100
        if remaining > 0:
            words.append(self._convert_two_digits(remaining))

        return " ".join(filter(None, words))
