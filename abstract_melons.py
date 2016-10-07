"""This file should have our order classes in it."""


class AbstractMelonOrder(object):
    """ You fill in the rest """


    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price."""

        base_price = 5

        if self.species == "christmas": 
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """ Sets order_type to domestic and tax .08. """

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """ Sets order_type to international and tax .17. Also returns country_code """

    order_type = "international"
    tax = 0.17

    #  These are the values that vary by order
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        self.country_code = country_code

        # Don't call the super with country_code because it's not expecting it
        # and it will be available directly from the instance that we're sending
        super(InternationalMelonOrder, self).__init__(species, qty)

    def get_country_code(self):
        """Return the country code."""

        return self.country_code



class GovernmentMelonOrder(AbstractMelonOrder):
    """ You fill in the rest """

    order_type = "government"
    tax = 0

    def __init__(self, species, qty, passed_inspection):
        """Initialize melon order attributes"""

        self.passed_inspection = False

        super(GovernmentMelonOrder, self).__init__(species, qty)

    def mark_inspection(self):
        """Set shipped to true."""

        self.passed_inspection = True
