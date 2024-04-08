class Coffee:
    def __init__(self, name):
        self.name = name

    # Create property method and return the name of the coffee
    @property
    def name(self):
        return self._name

    # Create setter and check if the name is a string and has a length of 3 or more
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "name") and len(name) >= 3:
            self._name = name
        # else:
        #     raise Exception

    # Return all orders for the coffee
    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    # Return all customers who have ordered the coffee
    def customers(self):
        return list(set([order.customer for order in self.orders()]))

    # Return the number of orders for the coffee
    def num_orders(self):
        return len(self.orders())

    # Return the average price of the coffee
    def average_price(self):
        return sum([order.price for order in self.orders()]) / self.num_orders()


class Customer:

    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    # Create property method and return the name of the customer
    @property
    def name(self):
        return self._name

    # Create setter and check if the name is a string and has a length of 1 to 15
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        # else:
        #     raise Exception

    # Return all orders for the customer
    def orders(self):
        return [order for order in Order.all if order.customer == self]

    # Return all coffees ordered by the customer
    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))

    # Return a new order for the customer
    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    # Return the total amount spent by the customer
    @classmethod
    def most_aficionado(cls, coffee):
        # Check if the input coffee is an instance of the Coffee class
        # if not isinstance(coffee, Coffee):
        #     raise Exception

        # Find all orders that have the input coffee
        if coffee_all_orders := [
            order for order in Order.all if order.coffee is coffee
        ]:
            # Find the customer with the highest total price of orders for the input coffee
            return max(
                cls.all,  # Use the all class attribute to get all customers
                key=lambda customer: sum(  # Use the sum function to get the total price of orders
                    order.price
                    for order in coffee_all_orders
                    if order.customer is customer
                ),
            )
        # Return None if there are no orders for the input coffee
        return None


class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    # Create property method and return the customer
    @property
    def price(self):
        return self._price

    # Create setter and check if the price is a float and is between 1 and 10
    @price.setter
    def price(self, price):
        if (
            isinstance(price, float)
            and not hasattr(self, "price")
            and 1.0 < price <= 10.0
        ):
            self._price = price
        # else:
        #     raise Exception

    # Create property method and return the customer
    @property
    def customer(self):
        return self._customer

    # Create setter and check if the customer is an instance of the Customer class
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        # else:
        #     raise Exception

    # Create property method and return the coffee
    @property
    def coffee(self):
        return self._coffee

    # Create setter and check if the coffee is an instance of the Coffee class
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        # else:
        #     raise Exception
