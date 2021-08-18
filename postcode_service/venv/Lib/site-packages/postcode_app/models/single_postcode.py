class PostCode():
    def __init__(self, postcodes_dict):
        self.pc = postcodes_dict
        self.latitude = self.pc['latitude']
        self.longitude = self.pc['longitude']
        self.eastings = self.pc['eastings']
        self.northings = self.pc['northings']

    def __repr__(self):
        return f"Postcode ({self.pc})"

    def get_location(self):
        return f"Latitude: {self.latitude}\n" \
               f"Longitude: {self.longitude}"
