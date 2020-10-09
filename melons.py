"""Classes for melon orders."""
class AbstractMelonOrder():

    def __init__(self, species, qty, order_type, tax):

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == 'Christmas':
            price = base_price * 1.5
        else:
            price = base_price

        fee = 0
        if self.qty < 10 and self.order_type == "international":
            fee = fee + 3
        
        total = (1 + self.tax) * self.qty * price + fee

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
        
    
class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, "international", 0.17)
        
    def get_country_code(self):
        """Return the country code."""

        return self.country_code
