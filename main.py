"""
Name: Gift Ogingo
Date: 25/02/2024
Brief Project Description:
GitHub URL: https://github.com/giftos1/TravelTrackerPart2

"""

# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, NumericProperty, ColorProperty
from kivy.uix.button import Button

from place import Place
from placecollection import PlaceCollection

INPUT_TO_ATTRIBUTE = {}
SPINNER_VALUES = ["visited", "priority", "country", "name"]
ORIGINAL_COLOR = (0, 0.6, 0.2)
ALTERNATE_COLOR = (0.5, 0.5, 1)


class TravelTrackerApp(App):
    """..."""
    status_text = StringProperty()
    place_values = ListProperty()
    status_number = NumericProperty()
    spinner_text = StringProperty()
    color = ColorProperty()

    def __init__(self, **kwargs):
        """Construct main Kivy app."""
        super().__init__(**kwargs)
        self.places_collection = PlaceCollection()
        # list of PlaceCollection objects from places.csv
        self.places_collection.load_places('places.csv')
        self.places = self.places_collection.places
        self.spinner_text = SPINNER_VALUES[0]
        self.place_values = SPINNER_VALUES
        self.status_text = f"Welcome to Travel Tracker 2.0"
        self.unvisited_count = self.places_collection.add_unvisited_places()
        self.status_number = self.unvisited_count

    def build(self):
        """create Widget instance"""
        Window.size = 1000, 700
        self.title = 'Travel Tracker'
        self.root = Builder.load_file('app.kv')
        self.create_widgets()
        return self.root

    def change_state(self, sort_value):
        """change sort value of spinner on select"""
        self.spinner_text = sort_value
        print("changed to", self.spinner_text)

    def create_widgets(self):
        """Create buttons from list of objects and add them to the GUI."""
        for place in self.places:
            # Create a button for each Place object, specifying the text
            if place.is_visited == "v":
                place_button = Button(text=f"{place.name} in {place.country}, priority {place.priority} (visited)")
                place_button.background_color = ORIGINAL_COLOR
            else:
                place_button = Button(text=f"{place.name} in {place.country}, priority {place.priority}")
                place_button.background_color = ALTERNATE_COLOR
            place_button.bind(on_release=self.press_entry)
            # Store a reference to the place object in the button object
            place_button.place = place
            self.places_collection.sort(self.spinner_text)
            print("spinner value", self.spinner_text)
            self.root.ids.entries_box.add_widget(place_button)


    def press_add(self, name, country, priority):
        """save a new entry to memory
        :param name: name text input (from app.kv)
        :param country: country (from app.kv)
        :param priority: priority (from app.kv)"""

        #  check for empty fields
        if self.root.ids.name.text == "" or self.root.ids.country.text == "" or self.root.ids.priority.text == "":
            self.status_text = "All fields must be completed!"

        # check if string is 0 or below 0
        elif self.root.ids.priority.text == "0" or (self.root.ids.priority.text.startswith('-')
                                                    and self.root.ids.priority.text[1:].isdigit()):
            self.status_text = "Priority must be > 0"

        # check if there are any letters in the string
        elif not self.root.ids.priority.text.isdigit():
            self.status_text = "Please enter a valid number"
        else:
            new_place = Place(name, country, priority, False)
            new_place.not_visited()  # mark new place as not visited(n)
            self.places_collection.add_place(new_place)

            # add button for new entry (same as in create_widgets())
            place_button = Button(text=f"{name} in {country}, priority {priority}")
            place_button.background_color = ALTERNATE_COLOR
            place_button.bind(on_release=self.press_entry)
            self.root.ids.entries_box.add_widget(place_button)
            self.clear_all()

            for place in self.places:
                place_button.place = place

    def press_entry(self, instance):
        """Handle pressing place buttons."""
        # Each button was given its own ".place" object reference, so we can get it directly
        place = instance.place
        print(self.spinner_text)
        # Update button text
        if place.is_visited == "v":
            place.is_visited = "n"
            self.status_text = f"You need to visit {place.name}."
            instance.background_color = ALTERNATE_COLOR
            self.status_number += 1
            instance.text = f"{place.name} in {place.country}, priority {place.priority}"
        else:
            self.status_text = f"You visited {place.name}. Great Travelling!"
            place.is_visited = "v"
            instance.background_color = ORIGINAL_COLOR
            self.status_number -= 1
            instance.text = f"{place.name} in {place.country}, priority {place.priority} (visited)"
        if place.is_visited == "n" and int(place.priority) <= 2:
            self.status_text = f"You need to visit {place.name}. Get going!"

    def on_stop(self):
        """save new state of places in places.csv"""
        self.places_collection.save_places('places.csv')

    def clear_all(self):
        """Clear all input fields and status text."""
        self.root.ids.name.text = ""
        self.root.ids.country.text = ""
        self.root.ids.priority.text = ""
        self.status_text = ""


if __name__ == '__main__':
    TravelTrackerApp().run()
