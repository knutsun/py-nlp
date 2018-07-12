import json
from json2html import *
import nlp
from prettytable import PrettyTable

with open('dictionary.json', 'r') as f:
	data = json.load(f)


x = PrettyTable()
x.field_names = ["Dutch", "Occurrences"]

for key in data.items():
	x.add_row(key)

with open('table.html', 'w') as f:
	f.write(x.get_html_string())