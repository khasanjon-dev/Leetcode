from geopy.geocoders import Nominatim

latitude = 41.283493
longitude = 69.210893
geolocator = Nominatim(user_agent="oqtepa")
location = geolocator.reverse(f"{latitude}, {longitude}")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw['address'])
print()
