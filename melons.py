import random
# from datetime import datetime
import datetime

"""Classes for melon orders."""


class AbstractiveMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    
    def __init__(self, species, qty) :

        self.order_type = None
        self.tax = 0
        self.species = species
        self.qty = qty
        self.shipped = False

        if self.qty > 100:
            raise TooManyMelonsError("No more than 100 melons!")
     


    def get_base_price(self):  
        """Splurge pricing function to choosing a random integer between 5-9 as the base price"""
        
        base_price = random.randint(5, 9) 
        order_inf = datetime.datetime.now()
        order_date = order_inf.strftime('%A')
        order_time = order_inf.strftime('%H')     

        morning_rush_price = 4
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        rush_hour = [8, 9, 10, 11]

        if order_date in weekdays and order_time in rush_hour:
            base_price += morning_rush_price

        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()        
        christmas_melon = base_price * 1.5        

        if self.species == "christmas melons":
            base_price = christmas_melon
        total = self.qty * base_price * (1 + self.tax)

        return total
   

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""                   

        self.shipped = True

class TooManyMelonsError(ValueError):
    """Raises an error when attempt to order more melon than allowed.""" 
    pass 

    # def raise_error(self):
    #     """return an error if order qty ultrapass 100"""

    #     if self.qty > 100:
    #         raise "No more than 100 melons!"



class  GovernmentMelonOrder(AbstractiveMelonOrder):
    """A Government Order"""      

    def __init__(self, species, qty):
        super().__init__(species, qty)

        self.passed_inspection = False


    def mark_inspection(self, passed):

        if passed == True:
            self.passed_inspection = True



class DomesticMelonOrder(AbstractiveMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)

        self.order_type = "domestic"
        self.tax = 0.08



class InternationalMelonOrder(AbstractiveMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self,species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        
        self.order_type = "international"
        self.tax = 0.17
        self.country_code = country_code

    

    def get_total(self):
        """Calculate price, including tax."""
        total_parent = super().get_total()

        flat_fee = 3
              
        if self.qty < 10:          
            total = total_parent + flat_fee
        else:    
            total = total_parent

        return total



    def get_country_code(self):
        """Return the country code."""

        return self.country_code    