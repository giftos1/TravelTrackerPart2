"""..."""
import csv
from operator import attrgetter

from place import Place


# Create your PlaceCollection class in this file


class PlaceCollection:

    def __init__(self):
        self.places = []

    def load_places(self, file):
        place_file = open(file, "r")
        for each_row in place_file:
            row = each_row.strip()
            rows = row.split(",")  # split each row in file to a list
            rows[2] = int(rows[2])  # convert number string to integer for sorting
            self.places.append(Place(rows[0], rows[1], rows[2], rows[3]))  # appending instances to list

    def save_places(self, file):
        place_file = open(file, "w", newline='')
        writer = csv.writer(place_file)
        writer.writerows(self.places)  # write places in file using csv module
        place_file.close()

    def add_place(self, place):
        return self.places.append(place)

    def add_unvisited_place(self, unvisited_count=0):
        for place in self.places:
            if "n" in place[3]:
                unvisited_count += 1
        return unvisited_count

    def sort(self, key, priority=None):
        if priority is None:
            self.places = sorted(self.places, key=attrgetter(key))
            return self.places
        else:
            self.places = sorted(self.places, key=attrgetter(key, priority))
            return self.places

    def __repr__(self):
        return repr(self.places)
