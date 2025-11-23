"""
IMPROVED Food Expenditure Cleaning Function
============================================

Handles all observed input formats comprehensively:
1. European formatting (periods as thousand separators)
2. Text descriptions (million, thousand, hundred thousand)
3. Range values with various formats
4. Comma separators
5. Text prefixes/suffixes
6. Mixed format ranges (European + text)

Critical fixes:
- Clean European format BEFORE extracting numbers
- Handle "Mill" abbreviation (not just "million" or "m")
- Properly parse European format ranges
"""

import pandas as pd
import numpy as np
import re

def clean_expenditure_value_IMPROVED(value):
    """
    Clean food expenditure values with comprehensive format handling.

    Returns: Float (in VND) or np.nan
    """
    if pd.isna(value):
        return np.nan

    # Convert to string and basic cleanup
    val_str = str(value).strip().lower()

    # Remove common prefixes/suffixes
    val_str = re.sub(r'^(around|about|approximately|roughly|approx)\s+', '', val_str)
    val_str = re.sub(r'\s+(de|vnd|dong|only|for|woman|man).*$', '', val_str)
    val_str = val_str.strip()

    # STEP 1: Detect if this contains "million", "mill", "thousand" text
    has_million = bool(re.search(r'(million|mill)\b', val_str)) or bool(re.search(r'\d+\s*m\s*$', val_str))
    has_thousand = bool(re.search(r'thousand', val_str)) or bool(re.search(r'\d+\s*k\s*$', val_str))

    # STEP 2: Pre-process European format (convert periods to nothing for extraction)
    # But preserve original for detection
    val_str_numeric = val_str

    # If European format detected (multiple periods OR single period with 3 digits after)
    if val_str.count('.') > 1 or re.search(r'\d+\.\d{3}(\D|$)', val_str):
        # This is European format - remove periods
        val_str_numeric = re.sub(r'\.(?=\d)', '', val_str)  # Remove periods before digits

    # STEP 3: Extract numbers from cleaned string
    numbers = re.findall(r'(\d+(?:,\d{3})*)', val_str_numeric)
    # Clean commas from extracted numbers
    numbers = [float(n.replace(',', '')) for n in numbers if n]

    if not numbers:
        return np.nan

    # STEP 4: Determine multiplier based on text
    multiplier = 1

    if has_million:
        multiplier = 1_000_000
    elif has_thousand:
        # Check for "hundred thousand"
        if 'hundred thousand' in val_str:
            # Number before "hundred thousand" is hundreds
            multiplier = 100_000
        else:
            multiplier = 1_000

    # STEP 5: Calculate final value
    if len(numbers) >= 2:
        # Range value - use midpoint
        numeric_val = (numbers[0] + numbers[1]) / 2
    else:
        # Single value
        numeric_val = numbers[0]

    result = numeric_val * multiplier

    return result


# Test function on all known formats
if __name__ == "__main__":
    test_cases = [
        # (input, expected, description)
        ('100.000', 100_000, 'European single period'),
        ('5.000.000', 5_000_000, 'European multiple periods'),
        ('Around 10.000.000', 10_000_000, 'European with text prefix'),
        ('2.000.000 - 3.000.000 de', 2_500_000, 'European range with suffix'),
        ('5 million', 5_000_000, 'Text million'),
        ('5 - 8 million', 6_500_000, 'Range with million'),
        ('7-8 Mill for only woman', 7_500_000, 'Range with Mill abbreviation'),
        ('7m', 7_000_000, 'Million abbreviation'),
        ('3 hundred thousand', 300_000, 'Spelled hundred thousand'),
        ('200,000', 200_000, 'Comma separator'),
        ('200000 - 300000', 250_000, 'Plain range'),
        ('5000000', 5_000_000, 'Plain numeric'),
        ('Around 100.000', 100_000, 'European with prefix'),
    ]

    print('='*80)
    print('IMPROVED CLEANING FUNCTION TEST RESULTS')
    print('='*80)
    print()

    all_passed = True
    for value, expected, description in test_cases:
        result = clean_expenditure_value_IMPROVED(value)
        passed = abs(result - expected) < 0.01 if not pd.isna(result) else False
        status = '✅ PASS' if passed else '❌ FAIL'

        if not passed:
            all_passed = False
            print(f'{status} | {value:30s} -> {result:>15,.0f} (expected {expected:>15,}) | {description}')
        else:
            print(f'{status} | {value:30s} -> {result:>15,.0f} | {description}')

    print()
    print('='*80)
    if all_passed:
        print('✅ ALL TESTS PASSED')
    else:
        print('❌ SOME TESTS FAILED - REVIEW FUNCTION')
    print('='*80)
