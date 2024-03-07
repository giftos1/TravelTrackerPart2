# Copy TravelTrackerPart1 to this file, then update it to use Place and PlaceCollection class

from place import Place
from placecollection import PlaceCollection

"""
Name:Gift Sydney Ogingo
GitHub URL:https://github.com/giftos1/TravelTrackerPart1
"""

FILENAME = 'places.csv'
NOT_VISITED = "n"
VISITED = "v"


def main():
    """Run the whole program"""

    print("Travel Tracker 2.0 - by Gift Ogingo")  # display welcome message

    place_collection = PlaceCollection()  # contains a list of Place objects
    place_collection.load_places('places.csv')  # load from csv file into Place objects in the list
    place_collection.sort("is_visited", "priority")  # sort by the key passed in then by priority

    print(len(place_collection.places), "places loaded from", FILENAME)

    menu_choices = ["l", "a", "m", "q"]

    menu_input = ""
    while menu_input != "q":
        places = place_collection.places
        menu_input = input("Menu:\n"
                           "L - List Places\n"
                           "A - Add new place\n"
                           "M - Mark a place as visited\n"
                           "Q - Quit\n"
                           ">>>").lower()

        if menu_input == "l":
            visit_statuses = [place.is_visited for place in places]
            if NOT_VISITED in visit_statuses:  # check if there are still any unvisited places
                get_max_name_length(places)
            else:
                print(len(places), "places. No places left to visit why not add a new place?")

        # Get name, country and priority input of a place and add them to the Travel Tracker
        elif menu_input == "a":
            name_input = validate_name_input()
            country_input = validate_country_input()
            get_priority(name_input, country_input, place_collection)  # Get priority input and check for ValueError

        elif menu_input == "m":
            visit_statuses = [place.is_visited for place in places]
            if NOT_VISITED in visit_statuses:  # check if there are still any unvisited places
                get_max_name_length(places)
                print("Enter the number of a place to mark as visited")
                place_number_input(places, place_collection)

            else:
                print("No unvisited places")

        elif menu_input not in menu_choices:
            print("Invalid menu choice")  # print result if user keys in a wrong input and start the loop again.

        else:
            print(f"{len(places)} places saved in places.csv")  # ends loop when user chooses q

    place_collection.save_places('places.csv')  # write nested list to file and close file

    print("Have a nice day:)")  # display message when user chooses q


def get_max_name_length(places):
    """get maximum length of city and country name in file and call display_formatted_list"""

    # add city and country names to respective lists
    city_names = [place.name for place in places]
    country_names = [place.country for place in places]

    max_country_length = len(max(country_names, key=len))
    max_city_length = len(max(city_names, key=len))

    return display_formatted_list(max_city_length, max_country_length, places)


def display_formatted_list(max_name_length, max_country_length, places):
    """Display a neatly formatted list of places when user chooses list"""
    unvisited_count = 0
    count = 0
    for place in places:
        count += 1

        additional_city_space = max_name_length - len(place.name)  # additional spaces to be added to line up a city
        # with
        # a shorter name length to the city with the longest name length

        additional_country_space = max_country_length - len(place.country)  # additional spaces to be added to line up a
        # country with a shorter name length to the country with the longest name length

        # display a dynamic lined up list based on longest city and country name.
        if len(place.name) != max_name_length and len(place.country) != max_country_length:

            # check if place is unvisited(n) and add a star(*) before the number if true
            # count the number of unvisited places
            if NOT_VISITED in place.is_visited:
                unvisited_count += 1
                print(f"*{count}.", place.name, "{:{}}in".format("", additional_city_space), place.country,
                      "{:{}}priority".format("", additional_country_space), place.priority)
            else:
                print(f" {count}.", place.name, "{:{}}in".format("", additional_city_space), place.country,
                      "{:{}}priority".format("", additional_country_space), place.priority)

        else:
            # No spaces are added if the city and country name's length is the maximum from the list of city_names and
            # country names in get_max_name_length() function

            if NOT_VISITED in place.is_visited:
                unvisited_count += 1
                print(f"*{count}.", place.name, "in", place.country, "priority", place.priority)
            else:
                print(f" {count}.", place.name, "in", place.country, "priority", place.priority)

    return display_visit_status(count, unvisited_count)


def display_visit_status(count, unvisited_count):
    """display the number of places visited and not visited"""
    return print(f"{count} places. You still want to visit {unvisited_count} places.")


def validate_name_input():
    """Get name input from user and check for blank answers"""
    name_input = ""
    validate_input = False
    while not validate_input:
        name_input = input("name: ")
        if not name_input.strip():
            print("Input can not be blank")
        else:
            validate_input = True
    return name_input


def validate_country_input():
    """Get country input from user and check for blank answers"""
    country_input = ""
    validate_input = False
    while not validate_input:
        country_input = input("Country: ")
        if not country_input.strip():
            print("Input can not be blank")
        else:
            validate_input = True
    return country_input


def get_priority(name_input, country_input, place_collection):
    """Get priority input and validate input
    Display the added place through printing the name,country and priority of the place"""
    validate_input = False
    priority_input = 0
    while not validate_input:
        try:
            priority_input = int(input("Priority: "))
            if priority_input <= 0:
                print("Number must be > 0")
            else:
                validate_input = True

        except ValueError:
            print("Invalid input; enter a valid number")

    print(f"{name_input} in {country_input} (priority {priority_input}) added to Travel Tracker")  # display added place
    return add_new_place(name_input, country_input, priority_input, place_collection)


def add_new_place(name, country, priority, place_collection):
    """Add new place to the nested list of places and sort the list accordingly"""

    new_place = Place(name, country, priority, False)
    new_place.not_visited()  # convert False to not visited(n)
    place_collection.add_place(new_place)
    place_collection.sort("is_visited", "priority")


def place_number_input(places, place_collection):
    """Validate the place number the user chooses to mark as visited. If place number is within range call
    convert_unvisited_place() """
    number_input = 0
    validate_input = False
    while not validate_input:
        try:
            number_input = int(input(">>>"))
            if number_input <= 0:
                print("Number must be > 0")

            elif number_input not in range(1, len(places) + 1):
                print("Invalid place number")

            else:
                validate_input = True

        except ValueError:
            print("Invalid input; enter a valid number")
    return convert_unvisited_place(number_input, places, place_collection)


def convert_unvisited_place(number_input, places, place_collection):
    """Convert unvisited place to visited if user marks it as visited"""
    for count, place in enumerate(places):
        count += 1
        while number_input == count:  # checks the number which the user types in that corresponds to a given place
            if place.is_visited == VISITED:
                print("That place is already visited!")
            else:
                place.is_visited = VISITED
                print(f"{place.name} in {place.country} visited!")
                place_collection.sort("is_visited", "priority")
            break


main()
