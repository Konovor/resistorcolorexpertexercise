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
   (4, 'black'): lambda first, second, third: f"{first}{second} ",
   (4, 'brown'): lambda first, second, third: f"{first}{second}0 ",
   (4, 'red'): lambda first, second, third: f"{first}{dot_cutoff(second)} kilo",
   (4, 'orange'): lambda first, second, third: f"{first}{second} kilo",
   (4, 'yellow'): lambda first, second, third: f"{first}{second}0 kilo",
   (4, 'green'): lambda first, second, third: f"{first}{dot_cutoff(second)} mega",
   (4, 'blue'): lambda first, second, third: f"{first}{second} mega",
   (4, 'violet'): lambda first, second, third: f"{first}{second}0 mega",
   (4, 'grey'): lambda first, second, third: f"{first}{dot_cutoff(second)} giga",
   (4, 'white'): lambda first, second, third: f"{first}{second} giga",
   (5, 'black'): lambda first, second, third: f"{first}{second}{third} ",
   (5, 'brown'): lambda first, second, third: f"{first}{dot_cutoff(second, third)} kilo",
   (5, 'red'): lambda first, second, third: f"{first}{second}{dot_cutoff(third)} kilo",
   (5, 'orange'): lambda first, second, third: f"{first}{second}{third} kilo",
   (5, 'yellow'): lambda first, second, third: f"{first}{dot_cutoff(second, third)} mega",
   (5, 'green'): lambda first, second, third: f"{first}{second}{dot_cutoff(third)} mega",
   (5, 'blue'): lambda first, second, third: f"{first}{second}{third} mega",
   (5, 'violet'): lambda first, second, third: f"{first}{dot_cutoff(second, third)} giga",
   (5, 'grey'): lambda first, second, third: f"{first}{second}{dot_cutoff(third)} giga",
   (5, 'white'): lambda first, second, third: f"{first}{second}{third} giga",
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

def dot_cutoff(*digits: int) -> str:
    if all(d == 0 for d in digits):
        return ""
    return "." + "".join(str(d) for d in digits).rstrip("0")

def resistor_label(colors: list[str]) -> str:
    num_bands = len(colors)
    if num_bands == 1:
        return '0 ohms'

    first_color, second_color, third_color, *unused = colors
    *unused, formatting_color, tolerance_color = colors

    first_digit = COLOR_TO_VALUE[first_color]
    second_digit = COLOR_TO_VALUE[second_color]
    third_digit = COLOR_TO_VALUE[third_color]

    formatting_rule = COLOR_TO_FORMATTING[num_bands, formatting_color]
    tolerance = COLOR_TO_TOLERANCE[tolerance_color]

    formatted = formatting_rule(first_digit, second_digit, third_digit)

    return f"{formatted}{UNIT} ±{tolerance}"
