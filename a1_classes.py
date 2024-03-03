# Copy TravelTrackerPart1 to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

from place import Place

"""
Name:Gift Sydney Ogingo
GitHub URL:https://github.com/giftos1/TravelTrackerPart1
"""
import csv
from operator import itemgetter

FILENAME = 'places.csv'
NOT_VISITED = "n"
VISITED = "v"


def main():
    """Run the whole program"""
    print("Travel Tracker 1.0 - by Gift Ogingo")  # display welcome message

    # load csv file and append sorted data to a nested list
    places = []
    place_file = open("places.csv", "r")
    for each_row in place_file:
        row = each_row.strip()
        rows = row.split(",")  # split each row in file to a list
        rows[2] = int(rows[2])  # convert number string to integer for sorting
        places.append(rows)

    places.sort(key=itemgetter(3, 2))  # sort list by visited status then priority
    print(len(places), "places loaded from", FILENAME)

    menu_choices = ["l", "a", "m", "q"]

    menu_input = ""
    while menu_input != "q":
        menu_input = input("Menu:\n"
                           "L - List Places\n"
                           "A - Add new place\n"
                           "M - Mark a place as visited\n"
                           "Q - Quit\n"
                           ">>>").lower()

        if menu_input == "l":
            place = [place for place in places]

            if NOT_VISITED in place[0][3]:  # check if there are still any unvisited places
                get_max_name_length(places)
            else:
                print(len(places), "places. No places left to visit why not add a new place?")

        # Get name, country and priority input of a place and add them to the Travel Tracker
        elif menu_input == "a":
            name_input = validate_name_input()
            country_input = validate_country_input()
            get_priority(name_input, country_input, places)  # Get priority input and check for ValueError

        elif menu_input == "m":
            place = [place for place in places]
            if NOT_VISITED in place[0][3]:  # check if there are still any unvisited places
                get_max_name_length(places)
                print("Enter the number of a place to mark as visited")
                place_number_input(places)

            else:
                print("No unvisited places")

        elif menu_input not in menu_choices:
            print("Invalid menu choice")  # print result if user keys in a wrong input and start the loop again.

        else:
            print(f"{len(places)} places saved in places.csv")  # ends loop when user chooses q

    # write nested list to file and close file
    place_file = open("places.csv", "w", newline='')
    writer = csv.writer(place_file)
    writer.writerows(places)  # write places in file using csv module
    place_file.close()

    print("Have a nice day:)")  # display message when user chooses q


def get_max_name_length(places):
    """get maximum length of city and country name in file and call display_formatted_list"""

    city_names = []
    country_names = []

    # add the name of each city and country to respective lists
    for each_place in places:
        city_name = each_place[0].strip("\n")
        city_names.append(city_name)

        country_name = each_place[1].strip("\n")
        country_names.append(country_name)

    # get the name of city and country with the maximum string length from respective lists
    max_country_length = len(max(country_names, key=len))
    max_city_length = len(max(city_names, key=len))

    return display_formatted_list(max_city_length, max_country_length, places)


def display_formatted_list(max_city_length, max_country_length, places):
    """Display a neatly formatted list of places when user chooses list"""
    unvisited_count = 0
    count = 0

    for place in places:
        count += 1

        additional_city_space = max_city_length - len(place[0])  # additional spaces to be added to line up a city with
        # a shorter name length to the city with the longest name length

        additional_country_space = max_country_length - len(place[1])  # additional spaces to be added to line up a
        # country with a shorter name length to the country with the longest name length

        # display a dynamic lined up list based on longest city and country name.
        if len(place[0]) != max_city_length and len(place[1]) != max_country_length:

            # check if place is unvisited(n) and add a star(*) before the number if true
            # count the number of unvisited places
            if "n" in place[3]:
                unvisited_count += 1
                print(f"*{count}.", place[0], "{:{}}in".format("", additional_city_space), place[1],
                      "{:{}}priority".format("", additional_country_space), place[2])
            else:
                print(f" {count}.", place[0], "{:{}}in".format("", additional_city_space), place[1],
                      "{:{}}priority".format("", additional_country_space), place[2])

        else:
            # No spaces are added if the city and country name's length is the maximum from the list of city_names and
            # country names in get_max_name_length() function

            if "n" in place[3]:
                unvisited_count += 1
                print(f"*{count}.", place[0], "in", place[1], "priority", place[2])
            else:
                print(f" {count}.", place[0], "in", place[1], "priority", place[2])

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


def get_priority(name_input, country_input, places):
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
    return new_added_place(name_input, country_input, priority_input, places)


def new_added_place(name, country, priority_input, places):
    """Add new place to the nested list of places and sort the list accordingly"""
    new_place = [name, country, priority_input, NOT_VISITED]
    places.append(new_place)
    places.sort(key=itemgetter(3, 2))


def place_number_input(places):
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
    return convert_unvisited_place(number_input, places)


def convert_unvisited_place(number_input, places):
    """Convert unvisited place to visited if user marks it as visited"""
    for count, place in enumerate(places):
        count += 1
        while number_input == count:  # checks the number which the user types in that corresponds to a given place
            if place[3] == VISITED:
                print("That place is already visited!")
            else:
                place[3] = VISITED
                print(f"{place[0]} in {place[1]} visited!")
                places.sort(key=itemgetter(3, 2))
            break


main()
