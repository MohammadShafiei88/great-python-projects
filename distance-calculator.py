from dataclasses import dataclass
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

@dataclass
class Coordinates:
    latitude: float
    longitude: float
    def coordinates(self):
        return self.latitude, self.longitude


def get_coordinates(address: str) -> Coordinates:
    geolocator = Nominatim(user_agent="distance-calculator")
    location = geolocator.geocode(address)
    if location:
        return Coordinates(latitude=location.latitude, longitude=location.longitude)


def calculate_distance_km(home: Coordinates, target: Coordinates):
    if home and target:
        distance: float = geodesic(home.coordinates(), target.coordinates()).kilometers
        return distance


def get_distance_km(home_address: str, target_address: str) -> float:
    home_coordinates: Coordinates = get_coordinates(home_address)
    target_coordinates: Coordinates = get_coordinates(target_address)

    if distance := calculate_distance_km(home_coordinates, target_coordinates):
        print(f'{home_address} -> {target_address}')
        print(f'Distance: {distance:.2f} km')
        return distance
    else:
        print('Failed to calculate the distance.')


def main():
    home_address: str = input('Enter an address: ')
    target_address: str = input('Enter an address: ')
    print(f'home address: {home_address}')
    print(f'target address: {target_address}')
    get_distance_km(home_address, target_address)

if __name__ == '__main__':
    main()

