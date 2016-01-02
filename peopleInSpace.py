import requests

url = requests.get("http://api.open-notify.org/astros.json")
numberOfAstro = url.json()

print("There are", str(numberOfAstro['number']), "in space right now.")
print("They are:")
for i in numberOfAstro['people']:
	print(i['name'])