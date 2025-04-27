"""
Core number to Nepali word conversion logic
"""


class NepaliNumberConverter:
    def __init__(self):
        self.units = ["", "एक", "दुई", "तीन", "चार", "पाँच", "छ", "सात", "आठ", "नौ"]
        self.tens = [
            "",
            "दस",
            "बीस",
            "तीस",
            "चालीस",
            "पचास",
            "साठी",
            "सत्तरी",
            "अस्सी",
            "नब्बे",
        ]
        self.hundreds = [
            "",
            "एक सय",
            "दुई सय",
            "तीन सय",
            "चार सय",
            "पाँच सय",
            "छ सय",
            "सात सय",
            "आठ सय",
            "नौ सय",
        ]
        self.thousands = ["", "हजार", "लाख", "करोड", "अरब", "खरब"]

        # Nepali numerals mapping
        self.nepali_numerals = {
            "0": "०",
            "1": "१",
            "2": "२",
            "3": "३",
            "4": "४",
            "5": "५",
            "6": "६",
            "7": "७",
            "8": "८",
            "9": "९",
        }

    def convert_to_nepali_words(self, number: int) -> str:
        """
        Convert a number to Nepali words
        """
        if number == 0:
            return "शून्य"

        if number < 0:
            return "ऋणात्मक " + self.convert_to_nepali_words(abs(number))

        words = []
        if number >= 1000:
            for i, unit in enumerate(self.thousands):
                if number % 1000 != 0:
                    words.append(self._convert_three_digits(number % 1000) + " " + unit)
                number = number // 1000
                if number == 0:
                    break
            words.reverse()
        else:
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
        nepali_num = "".join(self.nepali_numerals[digit] for digit in number_str)
        return f"{nepali_num} /-"

    def _convert_three_digits(self, number: int) -> str:
        """Convert a three-digit number to Nepali words"""
        if number == 0:
            return ""

        words = []
        hundred = number // 100
        if hundred > 0:
            words.append(self.hundreds[hundred])

        remaining = number % 100
        if remaining > 0:
            if remaining < 10:
                words.append(self.units[remaining])
            else:
                ten = remaining // 10
                unit = remaining % 10
                if ten > 0:
                    words.append(self.tens[ten])
                if unit > 0:
                    words.append(self.units[unit])

        return " ".join(filter(None, words))
