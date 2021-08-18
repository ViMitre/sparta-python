import requests


# postcode
# lat, long, eastings, northings
# __repr__ --> postcode shows


class PostCodeDict():
    def __init__(self, postcodes_dict):
        self.pc = postcodes_dict
        self.latitude = self.pc['latitude']
        self.longitude = self.pc['longitude']
        self.eastings = self.pc['eastings']
        self.northings = self.pc['northings']

    def __repr__(self):
        return f"Postcode ({self.pc})"

    def latlong(self):
        return f"Latitude: {self.latitude}\n" \
               f"Longitude: {self.longitude}"

    def easnor(self):
        return f"Eastings: {self.eastings}\n" \
               f"Northings: {self.northings}"


class PostCode():
    def __init__(self, postcode):
        self.pc = postcode
        self.postcode_url = "https://api.postcodes.io/postcodes/"
        postcode_url = "https://api.postcodes.io/postcodes/"
        self.postcode_request = requests.get(postcode_url + postcode)
        self.result = self.postcode_request.json()['result']
        self.latitude = self.result['latitude']
        self.longitude = self.result['longitude']
        self.eastings = self.result['eastings']
        self.northings = self.result['northings']

    def __repr__(self):
        return f"Postcode ({self.pc})"

    def latlong(self):
        return f"Latitude: {self.latitude}\n" \
               f"Longitude: {self.longitude}"

    def easnor(self):
        return f"Eastings: {self.eastings}\n" \
               f"Northings: {self.northings}"
