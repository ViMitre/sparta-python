import json

class RatesParser:
    def __init__(self, rates_filepath):
        self._open_json_file(rates_filepath)
        self.base = self._rates_info["base"]
        self.date = self._rates_info["date"]
        self.rates = self._rates_info["rates"]
        self.aud = self.rates["AUD"]
        self.gbp = self.rates["GBP"]
        self.usd = self.rates["USD"]


    def _open_json_file(self, filepath) -> dict:
        with open(filepath) as rates:
            self._rates_info = json.load(rates)

r = RatesParser("exchange_rates.json")

print(r.aud)