import robots


class Melon(object):
    """Melon."""

    def __init__(self, melon_type):
        """Initialize melon.

        melon_type: type of melon being built.
        """

        self.melon_type = melon_type
        self.weight = 0.0
        self.color = None
        self.stickers = []

    def prep(self):
        """Prepare the melon."""

        robots.cleanerbot.clean(self)
        robots.stickerbot.apply_logo(self)

    def __str__(self):
        """Print out information about melon."""

        if self.weight <= 0:
            return self.melon_type
        else:
            return f"{self.color} {self.weight:.2f} lbs {self.melon_type}"


# Add Squash class 
class Squash(Melon):
    
    # call super to inherit and initialize attributes of parent class Melon upon instantiation
    def __init__(self, melon_type):
        super().__init__(melon_type)
    
    # create pain method that inherits Melon prep method as we all as has paint functionality
    def paint(self):
        super().prep
        robots.painterbot.paint(self)
