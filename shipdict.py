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

    def __eq__(self, other):
        return self.id==other.id

    def __hash__(self):
        return hash((self.id,))


class ShipDict:
    def __init__(self):
        self.ships={}

    def add_chunk(self, chunk):
        if len(chunk)== 7:
            id,lat,lon,_,_,_,time=chunk
            ship=Ship(id)
        else:
            id,lat,lon,_,_,time,name,_,_,_,country,*_=chunk
            ship = Ship(id,name,country)
        position = Position(lat,lon,time)
        liste_positions=self.ships.setdefault(ship,[])
        liste_positions.append(position)


    def clean_unnamed(self):
        ships = self.ships.keys()
        to_remove=[]
        for ship in ships:
            if ship.name=='':
                to_remove.append(ship)
        for s in to_remove:
            self.ships.pop(s)

    def sort(self):
        self.ships=dict(sorted(self.ships.items(),key=lambda item :item[0].name))

    def all_ships(self):
        return list(self.ships.keys())

    def ships_by_name(self, ship_name):
        pass
