# aggregation (Has a relationship) >>> it means one class owns the other class >>>Private attributes cant be accessed using aggregation
class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def print_address(self):
        print(self.address.get_city(), self.address.pin, self.address.state)
        # print(self.address._Address__city)

    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.edit_address(new_city, new_pin, new_state)

class Address:
    def __init__(self, city, pin, state):
        self.__city = city
        self.pin = pin
        self.state = state

    def get_city(self):
        return self.__city

    def edit_address(self, new_city, new_pin, new_state):
        self.__city = new_city
        self.pin = new_pin
        self.state = new_state


add1 = Address("Srinagar", 191101, "J&K")
cust = Customer("Adnan", "Male", add1)

cust.print_address()
cust.edit_profile("Asrar", "Mumbai", 111111, "Punjab")
cust.print_address()

#AGGREATION CLASS DIAGRAM 