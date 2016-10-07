"""This file should have our order classes in it."""

import random
import datetime

class AbstractMelonOrder(object):
    """ You fill in the rest """


    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False

    # add an extra $4 charge to each melon ordered during morning rush hour 
    # (from 8-11am, Monday-Friday)
    def get_base_price(self):

        base_price = random.randint(5,9)

        now = datetime.datetime.today()

        day = now.weekday()
        time = now.hour

        # Check if today is Monday - Friday (0-4 in datetime)
        if day >= 0 and day < 5:
            # Check if time is between 8 and 11am.
            if time >= 8 and time < 11:
                # Increase base_price by 4
                base_price += 4


        return base_price

    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()

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

    # Don't call the super with passed_inspection because it's not expecting it
    # and it will be available directly from the instance that we're sending
    def __init__(self, species, qty, passed_inspection = False):
        """Initialize melon order attributes"""

        self.passed_inspection = passed_inspection

        super(GovernmentMelonOrder, self).__init__(species, qty)

    def mark_inspection(self, passed):
        """Set shipped to true."""

        if passed:
            self.passed_inspection = True
