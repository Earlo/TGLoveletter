CARDS = {}

def mapKeys(keys, value):
    temp = []
    for key in list(keys):
        CARDS[key] = value


localization ={ (1, "1", "guard"): 1,
            (2, "2", "priest"): 2,
            (3, "3", "baron"): 3,
            (4, "4", "handmaid"): 4,
            (5, "5", "prince"): 5,
            (6, "6", "king"): 6,
            (7, "7", "countess"): 7,
            (8, "8", "princess"): 8,
        }

for i in localization.keys():
    mapKeys( i, localization[i] )

NUM_TO_CARDS = {
    1: "Guard",
    2: "Priest",
    3: "Baron",
    4: "Handmaid",
    5: "Prince",
    6: "King",
    7: "Countess",
    8: "Princess"
}


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
