# Nepali Number to Word Converter

A Python package that converts numbers to Nepali words and numerals.

## Features

- Convert numbers to Nepali words (up to 99 खर्ब)
- Handle float values
- Convert numbers to Nepali numerals with proper formatting (१,२३,४५६ /-)
- Support for positive and negative numbers
- Proper error handling for unsupported numbers

## Installation

Install the package:
```bash
pip install nepali_number_to_word
```

## Usage

```python
from nepali_number_to_word import convert_to_nepali_words, convert_to_nepali_numerals


result = convert_to_nepali_words(123456789)
print(result)  # Output: बाह्र करोड चौतिस लाख छपन्न हजार सात सय उनान्नब्बे रूपैयाँ मात्र

result = convert_to_nepali_numerals(123456789)
print(result)  # Output: १२,३४,५६,७८९ /-

# Examples
print(convert_to_nepali_words(1234567.999))      # बाह्र लाख चौतिस हजार पाँच सय अठसट्ठी रुपैंया
print(convert_to_nepali_numerals(1234567.999))   # १२,३४,५६८ /-

# Examples
print(convert_to_nepali_words(123))      # एक सय तेइस रूपैयाँ मात्र
print(convert_to_nepali_numerals(123))   # १२३ /-



# Error handling
try:
    convert_to_nepali_words(1000000000000000)  # Raises ValueError
except ValueError as e:
    print(e)  # Numbers beyond 999,999,999,999,999 (99 खर्ब) are not supported
```

## Number Units

The converter supports the following Nepali number units:
- खर्ब (Kharab) = 100,000,000,000
- अरब (Arab) = 1,000,000,000
- करोड (Crore) = 10,000,000
- लाख (Lakh) = 100,000
- हजार (Thousand) = 1,000


## License

MIT License
