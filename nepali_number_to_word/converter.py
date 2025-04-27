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

        # Handle arab (अरब)
        arab = number // 1000000000
        if arab > 0:
            words.append(self._convert_number_part(arab) + " अरब")
            number = number % 1000000000

        # Handle crore (करोड)
        crore = number // 10000000
        if crore > 0:
            words.append(self._convert_number_part(crore) + " करोड")
            number = number % 10000000

        # Handle lakh (लाख)
        lakh = number // 100000
        if lakh > 0:
            words.append(self._convert_number_part(lakh) + " लाख")
            number = number % 100000

        # Handle thousand (हजार)
        thousand = number // 1000
        if thousand > 0:
            words.append(self._convert_number_part(thousand) + " हजार")
            number = number % 1000

        # Handle remaining hundreds
        if number > 0:
            words.append(self._convert_number_part(number))

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

    def _convert_number_part(self, number: int) -> str:
        """Convert any number part (1-99, 100-999, etc.) to Nepali words"""
        if number == 0:
            return ""

        if number < 100:
            return self._convert_two_digits(number)
        else:
            return self._convert_three_digits(number)

    def _convert_two_digits(self, number: int) -> str:
        """Convert a two-digit number to Nepali words"""
        if number == 0:
            return ""

        if number < 10:
            return UNITS[number]
        elif 10 <= number < 100:
            if number in range(10, 100):
                index = number - 10
                if index < len(SPECIAL_NUMBERS):
                    return SPECIAL_NUMBERS[index]
            ten = number // 10
            unit = number % 10
            if unit == 0:
                return TENS[ten]
            else:
                return TENS[ten] + " " + UNITS[unit]

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
            words.append(self._convert_two_digits(remaining))

        return " ".join(filter(None, words))
