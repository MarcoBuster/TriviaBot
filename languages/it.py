STRINGS = [
    {
        'start': '<b>Benvenuto nel bot</b>!\nStai usando la traduzione <b>italiana</b>'
    },
    {
        'q1': 'Chi è il creatore di questo bot?',
        'q1a1': '@MarcoBuster',
        'q1a2': '@AgeOfWar',
        'q1a3': '@Doksperiments',
        'q1a4': '@Giuseppina',


    }
]


def get(str_code):
    for string in STRINGS:
        for key in string:
            if key == str_code:
                return string[key]
