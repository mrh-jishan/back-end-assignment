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

    def get_room_mapping(self, optimized_min_room):
        room_list = []
        index = optimized_min_room
        while index:
            ad = int(self.adults / optimized_min_room) + 1 if (not (self.adults % optimized_min_room) == 0) and len(
                room_list) == 0 else int(
                self.adults / optimized_min_room)
            ch = int(self.children / optimized_min_room) + 1 if (not (self.children % optimized_min_room) == 0) and len(
                room_list) == 0 else int(
                self.children / optimized_min_room)
            inf = int(self.infants / optimized_min_room) + 1 if (not (self.infants % optimized_min_room) == 0) and len(
                room_list) == 0 else int(
                self.infants / optimized_min_room)

            room_list.append(Room(ad, ch, inf).__dict__)
            index -= 1

        return room_list

    def assign_room(self):
        # Calculate max required room for each category
        max_room_children = int(self.children / 3) if (self.children % 3) == 0 else int(self.children / 3) + 1
        max_room_infants = int(self.infants / 3) if (self.infants % 3) == 0 else int(self.infants / 3) + 1
        max_room_adult = int(self.adults / 3) if (self.adults % 3) == 0 else int(self.adults / 3) + 1

        # # Check if per booking has more than 3 room
        max_room = max_room_children if max_room_children >= max_room_infants else max_room_infants
        if max_room > 3: raise Exception('Per booking maximum number of rooms will be only 3')

        # # Check if any room has only infants or children
        if (self.adults < max_room): raise Exception('No room will have only children or infants')
        # Get final total number of most optimized room
        optimized_min_room = max_room if max_room >= max_room_adult else max_room_adult
        return optimized_min_room


booking = Booking(3, 4, 7)
optimized_min_room = booking.assign_room()
room_mapping = booking.get_room_mapping(optimized_min_room)
print('The optimized number of room(s): ', optimized_min_room)
print('The optimized room(s) mapping: ', room_mapping)
