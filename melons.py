"""Classes for melon orders."""


class AbstractiveMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty) :

        self.order_type = None
        self.tax = 0
        self.species = species
        self.qty = qty
        self.shipped = False


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        christmas_melon = base_price * 1.5        

        if self.species == "christmas melons":
            base_price = christmas_melon
        total = self.qty * base_price * (1 + self.tax)

        return total
   

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""                   

        self.shipped = True


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