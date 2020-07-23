class Vacancy:
    def __init__(self, title, location, salary, hours):
        self.tile = title
        self.location = location
        self.salary = salary
        self.hours = hours

    def __str__(self):
        return f"TITLE: {self.tile}, LOCATION: {self.location}, SALARY: {self.salary}, HOURS: {self.hours} \n"

    def __repr__(self):
        return self.__str__()