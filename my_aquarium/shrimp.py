
from my_aquarium.inhabitant_abc import BaseInhabitant

class Shrimp(BaseInhabitant):
    """A representation of a shrimp"""

    def __init__(self):
        pass

    @property
    def get_preferred_ph(self):
        """Returns the preferred PH"""
        return 7.2

    @property
    def get_preferred_temperature(self):
        return 28





