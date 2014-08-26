states = {
	"Oregon" : "OR",
	"Florida" : "FL",
	"California" : "CA",
	"New York:" : "NY",
	"Michigan" : "MI"
}

cities = {
	"CA" : "San Francisco",
	"MI" : "Detroit",
	"FL" : "Jacksonville"
}

cities["NY"] = "New York City"
cities["NY"] = "Buffalo"
cities["OR"] = "Portland"

def divider():
	print "_" * 10

divider
print "NY State has: ", cities["NY"]
print "OR State has: ", cities["OR"]

divider
print "Michigan's abbreviation is: ", states["Michigan"]
print "Florida's abbreviation is: ", states["Florida"]

divider
print "Michigan has: ", cities[states["Michigan"]]
print "Florida has: ", cities[states["Florida"]]

divider
for state, abbrev in states.items():
	print "%s is abbreviated %s." % (state, abbrev)
	
divider
for abbrev, city in cities.items():
	print "%s has the city %s." % (abbrev, city)
	
divider
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s." % (
		state, abbrev, cities[abbrev])
		
divider
state = states.get("Texas", None)

if not state:
	print "Sorry, no Texas."

city = cities.get("TX", "Does Not Exist")
print "The city for for the state 'TX' is: %s." % (city)