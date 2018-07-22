import json
from json2html import *
import nlp
from prettytable import PrettyTable

with open('dictionary.json', 'r') as f:
	data = json.load(f)


x = PrettyTable()
x.field_names = ["Dutch", "Occurrences"]
x.format = True

for key in data.items():
	x.add_row(key)

with open('table.html', 'w') as file:
	table = x.get_html_string(attributes={"id":"dictTable"})
	file.write('<link rel="stylesheet" href="style.css">')
	file.write(table)