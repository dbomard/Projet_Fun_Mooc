class Position:

    def __init__(self, latitude, longitude, time):
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = time


class Ship:

    def __init__(self, ship_id, name='', country=''):
        self.id = ship_id
        self.name = name
        self.country = country


class ShipDict:

    def add_chunk(self, chunk):
        pass

    def clean_unnamed(self):
        pass

    def sort(self):
        pass

    def all_ships(self):
        pass

    def ships_by_name(self, ship_name):
        pass
