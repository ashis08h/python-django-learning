# violates OCP


class Discount:

    def get_discount(self, customer_type):
        if customer_type == 'regular':
            return 5
        elif customer_type == 'VIP':
            return 10


# follow OCP


class Discount1:

    def get_discount(self):
        return 0


class RegularDiscount(Discount1):

    def get_discount(self):
        return 5


class VIPDiscount(Discount1):

    def get_discount(self):
        return 10
