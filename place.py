"""The Place class stores place data. The place data involves the name of the place, the country, priority and
the visit status"""


class Place:
    def __init__(self, name="", country="", priority=0, is_visited=""):
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    """print place data into csv in specified format"""
    def __str__(self):
        return f"{self.name},{self.country},{self.priority},{self.is_visited}"

    """mark place as not visited"""
    def not_visited(self):
        if not self.is_visited:
            self.is_visited = "n"
        return self.is_visited

    """mark place as visited"""
    def visited(self):
        if self.is_visited:
            self.is_visited = "v"
        return self.is_visited

    """determine if a place is important(having a priority <=2)"""
    def is_important(self, priority=2):
        if self.priority <= priority:
            return "important"
        else:
            return "not important"

    def __repr__(self):
        return f"['{self.name}', '{self.country}', '{self.priority}', '{self.is_visited}']"

