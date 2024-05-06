"""This PlaceCollection class contains a single attribute of places that is a list
of place objects. It also contains methods - load places, save places, add place,
sort and add unvisited places."""
from operator import attrgetter
from place import Place


class PlaceCollection:

    def __init__(self):
        self.places = []  # contains a list of Place objects

    def load_places(self, file):
        """load from csv file into Place objects in the list"""
        place_file = open(file, "r")
        for each_row in place_file:
            row = each_row.strip()
            rows = row.split(",")  # split each row in file to a list
            rows[2] = int(rows[2])  # convert number string to integer for sorting
            self.places.append(Place(rows[0], rows[1], rows[2], rows[3]))  # appending instances to list

    def add_place(self, place):
        """add a single Place object to the places attribute"""
        return self.places.append(place)

    def add_unvisited_places(self):
        """get number of unvisited places"""
        unvisited_count = 0
        for place in self.places:
            if place.is_visited == "n":
                unvisited_count += 1
        return unvisited_count

    def sort(self, key, priority=None):
        """sort by the key passed in then by priority"""
        if priority is None:
            self.places = sorted(self.places, key=attrgetter(key))
            return self.places
        else:
            self.places = sorted(self.places, key=attrgetter(key, priority))
            return self.places

    def save_places(self, file):
        """save from place list into csv file"""
        place_file = open(file, "w", newline='')
        for place in self.places:
            place_file.write(str(place) + "\n")  # write places in file using csv module
        place_file.close()

    def __repr__(self):
        """print a list of Place Objects"""
        return repr(self.places)
