CARDS = dict(map(
        (lambda (keys, value):
            temp = []
            for key in list(keys):
                temp.append((key, value))
            return temp
        ),
        {
            (1, "guard"): 1,
            (2, "priest"): 2,
            (3, "baron"): 3,
            (4, "handmaid"): 4,
            (5, "prince"): 5,
            (6, "king"): 6,
            (7, "countess"), 7,
            (8, "princess"), 8
        }.items()
    )
)

CARD_EMOJIS = {
    1:"💂‍♀️",
    2:"⛪️",
    3:"🕺",
    4:"👱‍♀️",
    5:"👨",
    6:"👑",
    7:"💃",
    8:"👸"
}
