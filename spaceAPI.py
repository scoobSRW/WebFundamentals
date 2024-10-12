import requests


# Fetch planet data from the Solar System OpenData API
def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    # Create a list to store planet details
    planet_list = []

    # Process each planet's information
    for planet in planets:
        if planet['isPlanet']:  # Check if the body is a planet
            name = planet.get('englishName', 'Unknown')
            mass = planet.get('mass', {}).get('massValue', 0)
            orbit_period = planet.get('sideralOrbit', 0)
            planet_list.append({
                'name': name,
                'mass': mass,
                'orbit_period': orbit_period
            })
            print(
                f"Planet: {name}, Mass: {mass} x 10^{planet.get('mass', {}).get('massExponent', 0)} kg, Orbit Period: {orbit_period} days")

    return planet_list


# Function to find the heaviest planet
def find_heaviest_planet(planets):
    heaviest_planet = max(planets, key=lambda p: p['mass'])
    return heaviest_planet['name'], heaviest_planet['mass']


# Fetch and print the planets data
planets = fetch_planet_data()

# Find and print the heaviest planet
name, mass = find_heaviest_planet(planets)
print(f"\nThe heaviest planet is {name} with a mass of {mass} x 10^24 kg.")


# You could also add more analysis like finding the planet with the longest orbit period:
def find_longest_orbit_planet(planets):
    longest_orbit_planet = max(planets, key=lambda p: p['orbit_period'])
    return longest_orbit_planet['name'], longest_orbit_planet['orbit_period']


# Find and print the planet with the longest orbit period
name, orbit_period = find_longest_orbit_planet(planets)
print(f"The planet with the longest orbit period is {name}, which takes {orbit_period} days to complete one orbit.")
