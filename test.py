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
print(converter.convert_to_nepali_words(123))  # एक सय बीस तीन रूपैयाँ मात्र
print(converter.convert_to_nepali_numerals(123))  # १२३ /-

print(converter.convert_to_nepali_words(100000))  # एक लाख रूपैयाँ मात्र
print(converter.convert_to_nepali_numerals(100000))  # १००००० /-

print(converter.convert_to_nepali_words(-1000))  # ऋणात्मक एक हजार रूपैयाँ मात्र
print(converter.convert_to_nepali_numerals(-1000))  # -१००० /-
