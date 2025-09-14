class ShowItemLocationDetails:

    def __init__(self, item, location):
        self.item = item
        self.location = location

    def info(self):
        print(f"My item is {self.item} and my location is {self.location}")


class FetchItemLocation(ShowItemLocationDetails):

    def __init__(self, item_location):
        super().__init__(item_location.split("_")[0], item_location.split("_")[1])











