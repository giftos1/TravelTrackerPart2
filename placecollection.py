"""This PlaceCollection class contains a single attribute of places that is a list
of place objects. It also contains methods - load places, save places, add place,
sort and add unvisited places."""
import csv
from operator import attrgetter

from place import Place


# Create your PlaceCollection class in this file


class PlaceCollection:

    def __init__(self):
        self.places = []  # contains a list of Place objects

    """load from csv file into Place objects in the list"""
    def load_places(self, file):
        place_file = open(file, "r")
        for each_row in place_file:
            row = each_row.strip()
            rows = row.split(",")  # split each row in file to a list
            rows[2] = int(rows[2])  # convert number string to integer for sorting
            self.places.append(Place(rows[0], rows[1], rows[2], rows[3]))  # appending instances to list

    """add a single Place object to the places attribute"""
    def add_place(self, place):
        return self.places.append(place)

    """get number of unvisited places"""
    def add_unvisited_places(self):
        unvisited_count = 0
        for place in self.places:
            if place.is_visited == "n" or not place.is_visited:
                unvisited_count += 1
        return unvisited_count

    """sort by the key passed in then by priority"""
    def sort(self, key, priority=None):
        if priority is None:
            self.places = sorted(self.places, key=attrgetter(key))
            return self.places
        else:
            self.places = sorted(self.places, key=attrgetter(key, priority))
            return self.places

    """save from place list into csv file"""
    def save_places(self, file):
        place_file = open(file, "w", newline='')
        writer = csv.writer(place_file)
        for place in self.places:
            writer.writerow([place])  # write places in file using csv module
        place_file.close()

    """print a list of Place Objects"""
    def __repr__(self):
        return repr(self.places)
