# violates OCP

class Discount:

    def get_discount(self, customer_type):
        if customer_type == 'regular':
            return 5
        elif customer_type == 'vip':
            return 10

# follow OCP

class Discount1:

    def get_discount(self):
        return 0


class RegularCustomer(Discount1):

    def get_discount(self):
        return 5


class VipCustomer(Discount1):

    def get_discount(self):
        return 10
