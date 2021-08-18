import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html")
# print(r)
c = r.content

html = BeautifulSoup(c, 'html.parser')
# print(html, type(html))

# print(html.prettify())

forex_table = html.find('table', {'class':'forextable'})
# print(forex_table)

table_body = forex_table.find('tbody')
# print(table_body.prettify())

table_rows = table_body.find_all('tr')
# print(table_rows)

forex_dict = {}

for row in table_rows:
    cells = row.find_all('td')
    for td in cells:
        if td.has_attr('id'):
            currency = td.find('a').text
        elif td.a.find('span'):
            rate = td.a.find('span').text
    forex_dict[currency] = rate

print(forex_dict)