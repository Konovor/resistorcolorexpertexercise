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

COLOR_TO_FORMATTING = {
   (4, 'black'): lambda first, second, third, tolerance: f"{first}{second} {UNIT} ±{tolerance}",
   (4, 'brown'): lambda first, second, third, tolerance: f"{first}{second}0 {UNIT} ±{tolerance}",
   (4, 'red'): lambda first, second, third, tolerance: f"{first}{dot_second(second)} kilo{UNIT} ±{tolerance}",
   (4, 'orange'): lambda first, second, third, tolerance: f"{first}{second} kilo{UNIT} ±{tolerance}",
   (4, 'yellow'): lambda first, second, third, tolerance: f"{first}{second}0 kilo{UNIT} ±{tolerance}",
   (4, 'green'): lambda first, second, third, tolerance: f"{first}{dot_second(second)} mega{UNIT} ±{tolerance}",
   (4, 'blue'): lambda first, second, third, tolerance: f"{first}{second} mega{UNIT} ±{tolerance}",
   (4, 'violet'): lambda first, second, third, tolerance: f"{first}{second}0 mega{UNIT} ±{tolerance}",
   (4, 'grey'): lambda first, second, third, tolerance: f"{first}{dot_second(second)} giga{UNIT} ±{tolerance}",
   (4, 'white'): lambda first, second, third, tolerance: f"{first}{second} giga{UNIT} ±{tolerance}",
   (5, 'black'): lambda first, second, third, tolerance: f"{first}{second}{third} {UNIT} ±{tolerance}",
   (5, 'brown'): lambda first, second, third, tolerance: f"{first}.{second}{third} kilo{UNIT} ±{tolerance}",
   (5, 'red'): lambda first, second, third, tolerance: f"{first}{second}.{third} kilo{UNIT} ±{tolerance}",
   (5, 'orange'): lambda first, second, third, tolerance: f"{first}{second}{third} kilo{UNIT} ±{tolerance}",
   (5, 'yellow'): lambda first, second, third, tolerance: f"{first}.{second}{third} mega{UNIT} ±{tolerance}",
   (5, 'green'): lambda first, second, third, tolerance: f"{first}{second}.{third} mega{UNIT} ±{tolerance}",
   (5, 'blue'): lambda first, second, third, tolerance: f"{first}{second}{third} mega{UNIT} ±{tolerance}",
   (5, 'violet'): lambda first, second, third, tolerance: f"{first}.{second}{third} giga{UNIT} ±{tolerance}",
   (5, 'grey'): lambda first, second, third, tolerance: f"{first}{second}.{third} giga{UNIT} ±{tolerance}",
   (5, 'white'): lambda first, second, third, tolerance: f"{first}{second}{third} giga{UNIT} ±{tolerance}",
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

def dot_second(second: int) -> str:
    return f".{second}" if second != 0 else ""

def resistor_label(colors: list[str]) -> str:
    num_bands = len(colors)
    if num_bands == 1:
        return '0 ohms'

    first_digit = COLOR_TO_VALUE[colors[0]]
    second_digit = COLOR_TO_VALUE[colors[1]]
    third_digit = COLOR_TO_VALUE[colors[2]]
    formatting_rule = COLOR_TO_FORMATTING[num_bands, colors[-2]]
    tolerance = COLOR_TO_TOLERANCE[colors[-1]]

    formatted = formatting_rule(first_digit, second_digit, third_digit, tolerance)

    return formatted
