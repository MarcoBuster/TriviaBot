STRINGS = [
    {'start': '<b>Benvenuto nel bot</b>!\nStai usando la traduzione <b>italiana</b>'}
]


def get(str_code):
    for string in STRINGS:
        for key in string:
            if key == str_code:
                return string[key]
