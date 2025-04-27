"""
Core number to Nepali word conversion logic
"""

from .constants import (
    UNITS,
    TENS,
    HUNDREDS,
    SPECIAL_NUMBERS,
    NEPALI_NUMERALS,
)


class NepaliNumberConverter:
    def __init__(self):
        pass

    def convert_to_nepali_words(self, number: int) -> str:
        """
        Convert a number to Nepali words
        """
        if number == 0:
            return "शून्य"

        if number < 0:
            return "ऋणात्मक " + self.convert_to_nepali_words(abs(number))

        words = []

        # Handle crore (करोड)
        crore = number // 10000000
        if crore > 0:
            words.append(self._convert_three_digits(crore) + " करोड")
            number = number % 10000000

        # Handle lakh (लाख)
        lakh = number // 100000
        if lakh > 0:
            words.append(self._convert_three_digits(lakh) + " लाख")
            number = number % 100000

        # Handle thousand (हजार)
        thousand = number // 1000
        if thousand > 0:
            words.append(self._convert_three_digits(thousand) + " हजार")
            number = number % 1000

        # Handle remaining hundreds
        if number > 0:
            words.append(self._convert_three_digits(number))

        result = " ".join(filter(None, words))
        return result.strip() + " रूपैयाँ मात्र"

    def convert_to_nepali_numerals(self, number: int) -> str:
        """
        Convert a number to Nepali numerals with /- suffix
        Example: 1000 -> १००० /-
        """
        if number < 0:
            return "-" + self.convert_to_nepali_numerals(abs(number))

        number_str = str(number)
        nepali_num = "".join(NEPALI_NUMERALS[digit] for digit in number_str)
        return f"{nepali_num} /-"

    def _convert_three_digits(self, number: int) -> str:
        """Convert a three-digit number to Nepali words"""
        if number == 0:
            return ""

        words = []
        hundred = number // 100
        if hundred > 0:
            words.append(HUNDREDS[hundred])

        remaining = number % 100
        if remaining > 0:
            if remaining < 10:
                words.append(UNITS[remaining])
            elif remaining <= 99:
                words.append(SPECIAL_NUMBERS[remaining - 10])
            else:
                ten = remaining // 10
                unit = remaining % 10
                if ten > 0:
                    words.append(TENS[ten])
                if unit > 0:
                    words.append(UNITS[unit])

        return " ".join(filter(None, words))
