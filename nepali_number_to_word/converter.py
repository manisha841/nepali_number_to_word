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
            special_numbers = [
                "दस",
                "एघार",
                "बाह्र",
                "तेह्र",
                "चौध",
                "पन्ध्र",
                "सोह्र",
                "सत्र",
                "अठार",
                "उन्नाइस",
                "बिस",
                "एक्काइस",
                "बाइस",
                "तेइस",
                "चौबिस",
                "पच्चिस",
                "छब्बिस",
                "सत्ताइस",
                "अट्ठाइस",
                "उनन्तिस",
                "तिस",
                "एकतिस",
                "बत्तिस",
                "तेत्तिस",
                "चौतिस",
                "पैँतिस",
                "छत्तिस",
                "सैँतिस",
                "अठतिस",
                "उनन्चालिस",
                "चालिस",
                "एकचालिस",
                "बयालिस",
                "त्रिचालिस",
                "चवालिस",
                "पैँतालिस",
                "छयालिस",
                "सतचालिस",
                "अठचालिस",
                "उनन्चास",
                "पचास",
                "एकाउन्न",
                "बाउन्न",
                "त्रिपन्न",
                "चवन्न",
                "पचपन्न",
                "छपन्न",
                "सन्ताउन्न",
                "अन्ठाउन्न",
                "उनसट्ठी",
                "साठी",
                "एकसट्ठी",
                "बयसट्ठी",
                "त्रिसट्ठी",
                "चौसट्ठी",
                "पैँसट्ठी",
                "छयसट्ठी",
                "सतसट्ठी",
                "अठसट्ठी",
                "उनन्सत्तरी",
                "सत्तरी",
                "एकहत्तर",
                "बहत्तर",
                "त्रिहत्तर",
                "चौहत्तर",
                "पचहत्तर",
                "छयहत्तर",
                "सतहत्तर",
                "अठहत्तर",
                "उनासी",
                "असी",
                "एकासी",
                "बयासी",
                "त्रियासी",
                "चौरासी",
                "पचासी",
                "छयासी",
                "सतासी",
                "अठासी",
                "उनान्नब्बे",
                "नब्बे",
                "एकान्नब्बे",
                "बयान्नब्बे",
                "त्रियान्नब्बे",
                "चौरान्नब्बे",
                "पन्चान्नब्बे",
                "छयान्नब्बे",
                "सन्तान्नब्बे",
                "अन्ठान्नब्बे",
                "उनान्सय",
            ]
            if remaining <= 99:
                words.append(special_numbers[remaining - 10])
            else:
                ten = remaining // 10
                unit = remaining % 10
                if ten > 0:
                    words.append(self.tens[ten])
                if unit > 0:
                    words.append(self.units[unit])

        return " ".join(filter(None, words))
