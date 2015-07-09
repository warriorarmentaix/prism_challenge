
import IPython

from geopy.geocoders import Nominatim
from geopy.distance import vincenty
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--cities", type=str, default="../data/cities.txt")
parser.add_argument("--useKM", type=bool, default=False)


args = parser.parse_args()


def deter_distance(cities):
	geolocator = Nominatim()
	distances = []
	for i in xrange(len(cities)-1):
		location1 = geolocator.geocode(cities[i])
		location2 = geolocator.geocode(cities[i+1])

		if location1 == None:
			print cities[i] + " could not be identified"
			raise ValueError
		if location2 == None:
			print cities[i+1] + " could not be identified"
			raise ValueError
		distance = vincenty((location1.latitude, location1.longitude), (location2.latitude, location2.longitude)).miles
		if args.useKM:
			distance = distance * 1.6
		distances.append(distance)

	return distances

f = open(args.cities, 'r')
cities = f.read().splitlines()
print cities

distances = deter_distance(cities)

units = ' kilometers' if args.useKM else ' miles'

print "Success! Your vacation itinerary is:"
for i in xrange(len(cities)-1):
	print cities[i] + ' -> ' + cities[i+1] + ': ' + str(distances[i]) + units

print "Total distance covered in your trip: " + str(sum(distances)) + units

