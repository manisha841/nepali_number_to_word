# Nepali Number to Word Converter

A Python package that converts numbers to Nepali words and numerals.

## Features

- Convert numbers to Nepali words
- Convert numbers to Nepali numerals (१, २, ३, etc.)
- Support for positive and negative numbers
- Simple and easy to use
- No external dependencies

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/nepali-number-to-word.git
cd nepali-number-to-word
```

2. Create a virtual environment and activate it:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install the package:
```bash
pip install -e .
```

## Usage

```python
from nepali_number_to_word import NepaliNumberConverter

# Create an instance of the converter
converter = NepaliNumberConverter()

# Convert numbers to Nepali words
result = converter.convert_to_nepali_words(1000)
print(result)  # Output: एक हजार रूपैयाँ मात्र

# Convert numbers to Nepali numerals
result = converter.convert_to_nepali_numerals(1000)
print(result)  # Output: १००० /-

# Examples
print(converter.convert_to_nepali_words(123))      # एक सय बीस तीन रूपैयाँ मात्र
print(converter.convert_to_nepali_numerals(123))   # १२३ /-

print(converter.convert_to_nepali_words(100000))   # एक लाख रूपैयाँ मात्र
print(converter.convert_to_nepali_numerals(100000)) # १००००० /-

print(converter.convert_to_nepali_words(-1000))    # ऋणात्मक एक हजार रूपैयाँ मात्र
print(converter.convert_to_nepali_numerals(-1000)) # -१००० /-
```

## Testing

Run the tests using pytest:
```bash
pytest
```

## License

MIT License
