"""..."""


# Create your Place class in this file


class Place:
    def __init__(self, name="", country="", priority=0, is_visited=""):
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def __str__(self):
        return f"{self.name} in {self.country} (priority {self.priority}) added to Travel Tracker"

    def not_visited(self, visit_status):
        if not visit_status:
            self.is_visited = "n"
        return self.is_visited

    def visited(self, visit_status):
        if visit_status:
            self.is_visited = "v"
        return self.is_visited

    def is_important(self, priority=2):
        if self.priority <= priority:
            return "important"
        else:
            return "not important"

    def __repr__(self):
        return '[{}, {}. {}, {}]'.format(self.name, self.country, self.priority, self.is_visited)

