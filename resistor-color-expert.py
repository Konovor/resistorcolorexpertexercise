COLOR_TO_VALUE = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9,
}

COLOR_TO_TOLERANCE = {
    'grey': '0.05%',
    'violet': '0.1%',
    'blue': '0.25%',
    'green': '0.5%',
    'brown': '1%',
    'red': '2%',
    'gold': '5%',
    'silver': '10%',
}

UNIT = 'ohms'

EXPONENT_TO_PREFIX = {
    6: 'kilo',# 4-band + red (2), 5-band + brown (1)
    7: 'kilo',# 4-band + orange (3), 5-band + red (2)
    8: 'kilo',# 4-band + yellow (4), 5-band + orange (3)
    9: 'mega',# 4-band + green (5), 5-band + yellow (4)
    10: 'mega',# 4-band + blue (6), 5-band + green (5)
    11: 'mega',# 4-band + violet (7), 5-band + blue (6)
    12: 'giga',# 4-band + grey (8), 5-band + violet (7)
    13: 'giga',# 4-band + white (9), 5-band + grey (8)
    14: 'giga',# 5-band + white (9)
}

def dot_cutoff(*digits: int) -> str:
    if all(d == 0 for d in digits):
        return ""
    return "." + "".join(str(d) for d in digits).rstrip("0")

# --- Formatting strategies ---

def format_2digit(first, second): return f"{first}{second}"
def format_2digit_zero(first, second): return f"{first}{second}0"
def format_2digit_dot(first, second): return f"{first}{dot_cutoff(second)}"

def format_3digit(first, second, third): return f"{first}{second}{third}"
def format_3digit_dot_last(first, second, third): return f"{first}{second}{dot_cutoff(third)}"
def format_3digit_dot_middle(first, second, third): return f"{first}{dot_cutoff(second, third)}"

COLOR_TO_FORMATTER = {
    (4, 'black'): format_2digit,
    (4, 'brown'): format_2digit_zero,
    (4, 'red'): format_2digit_dot,
    (4, 'orange'): format_2digit,
    (4, 'yellow'): format_2digit_zero,
    (4, 'green'): format_2digit_dot,
    (4, 'blue'): format_2digit,
    (4, 'violet'): format_2digit_zero,
    (4, 'grey'): format_2digit_dot,
    (4, 'white'): format_2digit,

    (5, 'black'): format_3digit,
    (5, 'brown'): format_3digit_dot_middle,
    (5, 'red'): format_3digit_dot_last,
    (5, 'orange'): format_3digit,
    (5, 'yellow'): format_3digit_dot_middle,
    (5, 'green'): format_3digit_dot_last,
    (5, 'blue'): format_3digit,
    (5, 'violet'): format_3digit_dot_middle,
    (5, 'grey'): format_3digit_dot_last,
    (5, 'white'): format_3digit,
}

def resistor_label(colors: list[str]) -> str:
    num_bands = len(colors)
    if num_bands == 1:
        return '0 ohms'

    if num_bands not in {4, 5}:
        raise ValueError(f"Unsupported number of bands: {num_bands}")

    digit_count = num_bands - 2
    digits = [COLOR_TO_VALUE[c] for c in colors[:digit_count]]
    multiplier_color = colors[-2]
    tolerance_color = colors[-1]

    formatter = COLOR_TO_FORMATTER[(num_bands, multiplier_color)]
    formatted = formatter(*digits)

    exponent = num_bands + COLOR_TO_VALUE[multiplier_color]
    prefix = EXPONENT_TO_PREFIX.get(exponent, '')

    tolerance = COLOR_TO_TOLERANCE[tolerance_color]

    return f"{formatted} {prefix}{UNIT} ±{tolerance}".strip()
