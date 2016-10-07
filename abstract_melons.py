"""This file should have our order classes in it."""



class AbstractMelonOrder(object):
    """ You fill in the rest """



    def __init__(self, species, qty, country_code = None):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        # Should this go here? 
        self.country_code = None

    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True




class DomesticMelonOrder(AbstractMelonOrder):
    """ You fill in the rest """

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """ You fill in the rest """

    order_type = "international"
    tax = 0.17
    # country_code = country_code


    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

