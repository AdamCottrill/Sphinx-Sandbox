class Tank:
    """My Aquarium.

    Fish and shrimps can live in it.
    The aquarium can be a freshwater or saltwater aquarium.

    We can adjust PH and temperature up or down.
    """

    def __init__(self, *, aquarium_type="freshwater", ph=7, temperature=30):
        """Initialize."""
        self.aquarium_type = aquarium_type
        self.ph = ph
        self.temperature = temperature
        self.stocks = []

    def stock_up(self, inhabitant, quantity):
        """Add more fish or shrimp to the tank.

        :param inhabitant: The type of inhabitant, either shrimp of fish
        :param quantity: The number of fish or shrimp to be added

        :raises TankIsFullError: if the tank is already full
        """
        pass

    def stock_down(self, inhabitant, quantity):
        """Take out some fish or shrimp from the tank."""
        pass

    def check_inhabitant_compatibility(self):
        """Check if this fish will be compatible with the current tank inhabitants."""
        return False

    def feed(self, food_type):
        pass

    @property
    def get_temperature(self):
        return f"{self.temperature} C"

    @property
    def get_ph(self):
        return self.ph

    def get_inhabitants(self):
        return self.stocks

    def ph_up(self):
        pass

    def ph_down(self):
        pass

    def temp_up(self):
        pass

    def temp_down(self):
        pass
