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

def normalize_color_code(colors: list[str]) -> list[str]:
    if len(colors) == 4:
        # prepending a zero aligns all further processing of 4 or 5 band resistors
        colors.insert(0, 'black')
    return colors

def resistor_label(colors: list[str]) -> str:
    if len(colors) == 1:
        return '0 ohms'

    colors = normalize_color_code(colors)

    first_digit = COLOR_TO_VALUE[colors[0]]
    second_digit = COLOR_TO_VALUE[colors[1]]
    third_digit = COLOR_TO_VALUE[colors[2]]
    fourth_digit = COLOR_TO_VALUE[colors[3]]
    tolerance = COLOR_TO_TOLERANCE[colors[4]]

    resistance_value = (first_digit * 100 + second_digit * 10 + third_digit) * (10 ** fourth_digit)

    # Format resistance without trailing zeros and proper unit

    if resistance_value >= 1_000_000_000:
        resistance = f"{resistance_value / 1_000_000_000:g} giga"
    elif resistance_value >= 1_000_000:
        resistance = f"{resistance_value / 1_000_000:g} mega"
    elif resistance_value >= 1_000:
        resistance = f"{resistance_value / 1_000:g} kilo"
    else:
        resistance = f"{resistance_value:g} "

    return f"{resistance}{UNIT} ±{tolerance}"
