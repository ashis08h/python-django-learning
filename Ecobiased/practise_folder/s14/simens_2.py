class ShowItemLocation:

    def __init__(self, item, location):
        self.item = item
        self.location = location

    def info(self):
        return f"My item is {self.item} and location is {self.location}"


class FetchLocation(ShowItemLocation):

    def __init__(self, item_location):
        super().__init__(item_location.split("_")[0], item_location.split("_")[0])


sil = ShowItemLocation("item", "location")
print(sil.item)
print(sil.location)

fl = FetchLocation("item_location")
print(fl.item)
print(fl.location)