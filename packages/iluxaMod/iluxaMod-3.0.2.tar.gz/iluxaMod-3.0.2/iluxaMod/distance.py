

class Distance:
    def __init__(self, lat1, lon1, lat2, lon2):
        self.lat1 = lat1
        self.lon1 = lon1
        self.lat2 = lat2
        self.lon2 = lon2

    def get_distance(self):
        from geopy.distance import great_circle

        locationA = (self.lat1, self.lon1)
        locationB = (self.lat2, self.lon2)
        return round(great_circle.geodesic(locationA, locationB).km, 3)
