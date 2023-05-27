class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

        coffee.orders(self)
        coffee.customers(customer)

        customer.orders(self)
        customer.coffees(coffee)

    def get_price(self):
        return self._price
    
    def set_price(self, price):
        if not isinstance(price, int) and 1 <= price <= 10:
            raise Exception
        else:
            self._price = price

    price = property(get_price, set_price)

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        from classes.customer import Customer
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        from classes.coffee import Coffee
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception