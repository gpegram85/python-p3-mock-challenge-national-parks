class NationalPark:

    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) <= 3:
            raise AttributeError("Name must be a string atleast 3 characters in length.")
        self._name = name
        NationalPark.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, "_name"):
            raise AttributeError("Cannot modify name after instantiation.")
        self._name = value
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list({park.visitor for park in self.trips()})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitor_count = {}
        for trip in self.trips():
            visitor = trip.visitor
            if visitor in visitor_count:
                visitor_count[visitor] += 1
            else:
                visitor_count[visitor] = 1
        return max(visitor_count, key=visitor_count.get, default=None)

class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        if not isinstance(visitor, Visitor):
            raise AttributeError("Visitor must be a Visitor instance.")
        if not isinstance(national_park, NationalPark):
            raise ValueError("National Park must be a National Park instance.")
        self._visitor = visitor
        self._national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, date):
        if not isinstance(date, str) or 7 > len(date):
            raise AttributeError("Date must be a string greater than 7 characters.")
        self._start_date = date

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, date):
        if not isinstance(date, str) or 7 > len(date):
            raise AttributeError("Date must be a string greater than 7 characters.")
        self._end_date = date

    @property
    def national_park(self):
        return self._national_park
    
    @property
    def visitor(self):
        return self._visitor

class Visitor:

    all = []

    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise AttributeError("Name must be a string between 1 and 15 characters long.")
        self._name = name
        Visitor.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise AttributeError("Name must be a string between 1 and 15 characters long.")
        self._name = value

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list({visitor.national_park for visitor in self.trips()})
    
    def total_visits_at_park(self, park):
        pass