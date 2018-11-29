class Room:
    def __init__(self, adults, children, infants):
        if adults > 3: raise ValueError('Max 3 adults allowed')
        if children > 3: raise ValueError('Max 3 children allowed')
        if infants > 3: raise ValueError('Max 3 infants allowed')
        if adults < 1: raise Exception('Minimum 1 adult is required, No room will have only children or infants')
        self.adults = adults
        self.children = children
        self.infants = infants


class Booking:
    def __init__(self, adults, children, infants):
        if (adults + children) > 7: raise ValueError('Max 7 people excluding infants')
        self.adults = adults
        self.children = children
        self.infants = infants

    @property
    def adults(self):
        return self._adults

    @adults.setter
    def adults(self, d):
        if not d: raise ValueError('Minimum 1 adult is required')
        self._adults = d

    def assign_room(self):
        max_room_children = int(self.children / 3) if (self.children % 3) == 0 else int(self.children / 3) + 1
        max_room_infants = int(self.infants / 3) if (self.infants % 3) == 0 else int(self.infants / 3) + 1
        max_room_adult = int(self.adults / 3) if (self.adults % 3) == 0 else int(self.adults / 3) + 1

        max_room = max_room_children if max_room_children >= max_room_infants else max_room_infants
        if (self.adults < max_room): raise Exception('No room will have only children or infants')
        max_room = max_room if max_room >= max_room_adult else max_room_adult

        # room_list = []
        # booking1 = {1: Room(3, 3, 3)}
        # booking2 = {2: Room(3, 3, 3)}
        #
        # room_list.append(booking1)
        # room_list.append(booking2)
        # print(booking1.__dict__)
        # total_room_adult = (self._adults % 3) if (self._adults % 3) == 0 else (self._adults % 3) + 1
        return dict({'total_room': max_room})


booking = Booking(7, 0, 14)
room_details = booking.assign_room()
print(room_details)
