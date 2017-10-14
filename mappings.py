def mapKeys(keys, value):
    temp = []
    for key in list(keys):
        temp.append((key, value))
    return temp

CARDS = dict(map(
        (mapKeys
        ),
        {
            (1, "1", "guard"): 1,
            (2, "2", "priest"): 2,
            (3, "3", "baron"): 3,
            (4, "4","handmaid"): 4,
            (5, "5", "prince"): 5,
            (6, "6", "king"): 6,
            (7, "7", "countess"), 7,
            (8, "8", "princess"), 8
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
