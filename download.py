import functions
import json

with open('aulas.json') as aulax:
	aulas = json.load(aulax)

	print(aulas)