# latitude = 41.283767
# longitude = 69.210916
#
# import googlemaps
#
# gmaps = googlemaps.Client(key=key)
# reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude))
# if reverse_geocode_result:
#     for result in reverse_geocode_result:
#         print("Formatted Address:", result['formatted_address'])
#
#         for component in result['address_components']:
#             print(f"{component['types'][0].capitalize()}: {component['long_name']}")
#
#             # Check for street number and name
#             if 'street_number' in component['types']:
#                 street_number = component['long_name']
#                 print(f"Street Number: {street_number}")
#             elif 'route' in component['types']:
#                 street_name = component['long_name']
#                 print(f"Street Name: {street_name}")
#
#         print("Place ID:", result['place_id'])
#         print("Types:", result['types'])
#         print("\n---\n")
# else:
#     print("No results found.")

from geopy.geocoders import Nominatim

latitude = 41.283493
longitude = 69.210893
geolocator = Nominatim(user_agent="oqtepa")
location = geolocator.reverse(f"{latitude}, {longitude}")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw['address'])
print()