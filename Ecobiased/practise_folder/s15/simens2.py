class ShowItemLocation:

    def __init__(self, item, location):
        self.item = item
        self.location = location

    def info(self):
        return f"My item is {self.item} and my location is {self.location}"


class FetchItemLocation(ShowItemLocation):

    def __init__(self, item_location):
        self.item_location = item_location
        super().__init__(self.item_location.split("_")[0], self.item_location.split("_")[1])


sil = ShowItemLocation("Item1", "Location1")
print(sil.info())

fil = FetchItemLocation("Item2_Location2")
print(fil.info())