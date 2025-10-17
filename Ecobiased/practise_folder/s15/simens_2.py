class ShowItemLocation:

    def __init__(self, item, location):
        self.item = item
        self.location = location

    def info(self):
        return f"My item is {self.item} and location is {self.location}"


class FetchLocation(ShowItemLocation):

    def __init__(self, item_location):
        super().__init__(item_location.split("_")[0], item_location.split("_")[1])


sil = ShowItemLocation("car", "Munger")
print(sil.item)
print(sil.location)

fl = FetchLocation("car_munger")
print(fl.item)
print(fl.location)