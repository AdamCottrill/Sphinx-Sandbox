from my_aquarium.inhabitant_abc import BaseInhabitant


class Fish(BaseInhabitant):
    """A representation of a fish."""
    def __init__(self):
        pass

    @property
    def get_preferred_ph(self):
        return 7

    @property
    def get_preferred_temperature(self):
        return 30





