"""
The item class represents either: locked slots, usable slots, plants, animals, fertilizer, watering
can
"""

class Item:

    def __init__(self):
        self.name = "NAME"
        self.co2saved = 0  # CO2 savings since planting
        self.growingfactor = 0.  # how fast the item grows
        self.co2consumption = 0.  # how much CO2 the item consumes
        self.indefinite = True  # whether the item stays indefinitely (until redeemed)
        self.drop = False  # whether the item has a drop to collect
        self.lifetime = -1.  # how long the item stays. negative values
        self.picture = None  # the picture of the item