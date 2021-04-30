class Position:

    def __init__(self, latitude, longitude, time):
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = time

    def __repr__(self):
        mnt, sec = divmod(abs(self.latitude)*3600,60)
        deg, mnt = divmod(mnt, 60)
        latitude = f"{int(deg):02}.{int(mnt):02}'{int(sec):02}'' "+('N' if self.latitude>0 else 'S ')
        mnt, sec = divmod(abs(self.longitude)*3600,60)
        deg, mnt = divmod(mnt,60)
        longitude = f"{int(deg):02}.{int(mnt):02}'{int(sec):02}'' "+('E' if self.longitude>0 else 'W ')
        return '<'+latitude+longitude+f'@ {self.timestamp}'+'>'


class Ship:

    def __init__(self, ship_id, name='', country=''):
        self.id = ship_id
        self.name = name
        self.country = country
        self.positions = []

    def __eq__(self, other):
        return self.id==other.id

    def __hash__(self):
        return hash((self.id,))
    
    def sort_positions(self):
        self.positions.sort(key=lambda position:position.timestamp)
        
    def add_position(self, position):
        self.positions.append(position)
        self.positions=list(set(self.positions))


class ShipDict:
    def __init__(self):
        self.ships={}

    def add_chunk(self, chunk):
        if len(chunk) == 7:
            id,lat,lon,_,_,_,time=chunk
            if id not in self.ships:
                self.ships[id]=Ship(id)
        else:
            id,lat,lon,_,_,time,name,_,_,_,country,*_=chunk
            if id in self.ships:
                if self.ships[id].name=='':
                    self.ships[id].name = name
            else:
                self.ships[id]=Ship(id,name,country)
        self.ships[id].add_position(Position(lat,lon,time))
        #TODO : Change the creation of the dictionnary to have dict{ship_id:ship}

    def clean_unnamed(self):
        ships = self.ships.values()
        to_remove=[]
        for ship in ships:
            if ship.name == '':
                to_remove.append(ship)
        for s in to_remove:
            self.ships.pop(s.id)

    def sort(self):
        for ship in self.ships.values():
            ship.sort_positions()

    def all_ships(self):
        return list(self.ships.values())

    def ships_by_name(self, ship_name):
        return [ship for ship in self.ships.values() if ship.name==ship_name]
