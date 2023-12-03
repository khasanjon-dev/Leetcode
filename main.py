from geopy.geocoders import Nominatim

latitude = 41.283493
longitude = 69.210893


def get_address(latitude: float, longitude: float):
    geolocator = Nominatim(user_agent="oqtepa")
    location = geolocator.reverse(f"{latitude}, {longitude}")
    address = location.raw['address']
    house_number = address.get('house_number', None)
    road = address.get('road', None)
    region = address.get('county', None)
    city = address['city']
    return address


print(get_address(latitude, longitude))
